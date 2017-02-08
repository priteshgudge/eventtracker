# -*- coding: utf-8 -*-

import csv
import json
import logging
import sys

from agro_db.catalog_management.models import *
from catalogservicev2.utils.get_displayable_product_details import get_displayable_product_attributes
from catalogservicev2.utils.update_images import *
from django.db import transaction

logger = logging.getLogger('main')


mandatory_fields = ['Product Name', 'C3', 'C2', 'C1', 'SKU Code', 'Price', 'Brand', 'Manufacturer', "Language"]
ignore_list = {'Product Name', 'C3', 'C2', 'C1', 'SKU Code', 'Price', 'Product Name_short', "Language"}

valid_language = set([l.language_code for l in Language.objects.all()])
valid_brands = set([t.brand_name.lower().strip(" ") for t in ProductBrand.objects.all()])
valid_manufacturers = set([t.product_manufacturer.lower().strip(" ") for t in ProductManufacturer.objects.all()])


def update_product_attributes(record, catalog_obj, language_code_source):
    language_obj = Language.objects.get(language_code=language_code_source)

    for key in record:
        logger.info("Setting values for attribute {}".format(key))
        k_value = record[key]
        if key in ignore_list:
            continue

        attribute = ProductAttributeKey.objects.get(attribute_name=key)

        try:
            value_obj = ProductAttributeValues.objects.get(
                product_catalog=catalog_obj,
                product_attribute_key=attribute,
                language=language_obj)
            value_obj.value = k_value
            value_obj.save()
            logger.debug("Updated {}".format(value_obj))
        except:
            value_obj = ProductAttributeValues.objects.create(
                product_catalog=catalog_obj,
                product_attribute_key=attribute,
                value=k_value,
                language=language_obj)
            logger.debug("Created {}".format(value_obj))

    attributes_str = get_displayable_product_attributes(catalog_obj, language_obj)
    l_description = catalog_obj.product_desciprion.filter(language=language_obj)[0]
    l_description.description = json.dumps(attributes_str)
    l_description.product_name = record['Product Name']
    l_description.save()

def validate_languages(content):
    languages = set([row['Language'] for row in content])
    diff = languages.difference(valid_language)
    if diff:
        raise ValueError("Invalid language codes : {}".format(diff))

def validate_brands(english_rows):
    brands = set(map(lambda x: x['Brand'].lower().strip(" "), english_rows))
    diff = brands.difference(valid_brands)

    if diff:
        invalid_brands = [x['Brand'] for x in english_rows if x['Brand'].lower().strip(" ") in diff]
        raise ValueError("Invalig Brands : {}".format(invalid_brands))

def validate_manufacturer(english_rows):
    manufacturers = set(map(lambda x: x['Manufacturer'].lower().strip(" "), english_rows))
    diff = manufacturers.difference(valid_manufacturers)

    if diff:
        invalid_manufacturer = [x['Manufacturer'] for x in english_rows if x['Manufacturer'].lower().strip(" ") in diff]
        raise ValueError("Invalid manufacturer : {}".format(invalid_manufacturer))


def resolve_category(c1, c2, c3):
    try:
        cat_1 = ProductCategory.objects.get(category_name=c1)
    except:
        return None

    if c2 == "" or c2 == None:
        return cat_1

    try:
        cat_2 = ProductCategory.objects.get(category_name=c2, parent_id=cat_1.id)
    except:
        return None

    if c3 == "" or c3 == None:
        return cat_2

    try:
        cat_3 = ProductCategory.objects.get(category_name=c3, parent_id=cat_2.id)
        return cat_3
    except:
        return None


def validate_categories(english_rows):
    for row in english_rows:
        c1, c2, c3 = row['C1'], row['C2'], row['C3']
        if not resolve_category(c1, c2, c3):
            raise ValueError("Category are invalid")


def create_catalog_object(record):
    logging.info("create_catalog_object {} {}".format(record['SKU Code'], record['Language']))
    sku = record['SKU Code'].strip()

    brand = record['Brand']
    manufacturer = record['Manufacturer']

    mrp = record['MRP'].strip() or "0"
    selling_price = record['Price'].strip() or "0"

    brand_obj = ProductBrand.objects.get(brand_name=brand)
    manufacturer_obj = ProductManufacturer.objects.get(product_manufacturer=manufacturer)
    weight_unit_obj = ProductWeightAttribute.objects.get(weight_unit_english='gm')

    c1, c2, c3 = record['C1'], record['C2'], record['C3']
    category = resolve_category(c1, c2, c3)
    weight_s = record['Weight'].strip() or "0"
    weight_unit = record['Unit'].strip() or "gm"

    try:
        weight_unit_obj = ProductWeightAttribute.objects.get(weight_unit_english=weight_unit)
    except:
        weight_unit_obj = ProductWeightAttribute.objects.get(weight_unit_english="gm")

    try:
        weight_val = float(weight_s)
    except:
        weight_val = 0

    catalog_obj = ProductCatalog.objects.create(sku_code=sku,
                                                product_category=category,
                                                product_brand=brand_obj,
                                                product_manufacturer=manufacturer_obj,
                                                weight=weight_val,
                                                weight_unit=weight_unit_obj,
                                                mrp=mrp,
                                                selling_price=selling_price)

    create_all_images(catalog_obj)
    return catalog_obj


def push_english_record(record):
    sku = record['SKU Code'].strip()

    try:
        catalog_obj = ProductCatalog.objects.get(sku_code=sku)
        logger.info("Updated = {}".format(sku))
    except:
        catalog_obj = create_catalog_object(record)
        logger.info("Created = {}".format(sku))

    weight_s = record['Weight'].strip() or "0"
    weight_unit = record['Unit'].strip() or "gm"

    try:
        weight_unit_obj = ProductWeightAttribute.objects.get(weight_unit_english=weight_unit)
    except:
        weight_unit_obj = ProductWeightAttribute.objects.get(weight_unit_english="gm")

    try:
        weight_val = float(weight_s)
    except:
        weight_val = 0

    catalog_obj.weight = weight_val
    catalog_obj.weight_unit = weight_unit_obj

    brand = record['Brand']
    manufacturer = record['Manufacturer']

    brand_obj = ProductBrand.objects.get(brand_name=brand)
    manufacturer_obj = ProductManufacturer.objects.get(product_manufacturer=manufacturer)

    catalog_obj.product_brand = brand_obj
    catalog_obj.product_manufacturer = manufacturer_obj

    c1, c2, c3 = record['C1'], record['C2'], record['C3']
    category = resolve_category(c1, c2, c3)
    catalog_obj.product_category = category

    catalog_obj.save()

    update_product_attributes(record, catalog_obj, "en")


def push_other_language_record(record):
    logger.info("push_other_language_record {} {}".format(record['SKU Code'], record['Language']))

    sku = record['SKU Code'].strip()
    try:
        catalog_obj = ProductCatalog.objects.get(sku_code=sku)
    except:
        raise ValueError("Catalog object missing : {}".format(sku))

    update_product_attributes(record, catalog_obj, record["Language"])
    catalog_obj.enabled_for_app = True
    catalog_obj.save()

    logger.info("Updated details: {} {}".format(sku, record["Language"]))


def push_single_record(record):
    language = record['Language']
    logger.info("Processing : {} for {}".format(record['SKU Code'], language))
    if language == 'en':
        return push_english_record(record)
    else:
        return push_other_language_record(record)


@transaction.atomic()
def main(source_file):
    csvfile = open(source_file)
    reader = csv.DictReader(csvfile)

    logger.info("Validating product info...")

    content = [row for row in reader]
    english_content = filter(lambda x: x['Language'] == 'en', content)

    validate_languages(content)

    validate_brands(english_content)

    validate_manufacturer(english_content)

    validate_categories(english_content)

    logger.info("Updating products...")
    for i, row in enumerate(content):
        logger.info("{}. row = {}".format(i, row))
        push_single_record(row)

    logger.info("done.")


if __name__ == '__main__':
    source_file = sys.argv[1]
    main(source_file)
