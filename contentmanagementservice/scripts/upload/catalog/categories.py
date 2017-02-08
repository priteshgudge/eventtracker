# -*- coding: utf-8 -*-

import django
import csv
import logging
import sys
django.setup()

from agro_db.catalog_management.models import *
from django.db import transaction

logger = logging.getLogger('main')


def resolve_category(c1, c2, c3):
    try:
        cat_1 = ProductCategory.objects.get(category_name=c1)
    except:
        return None

    if c2 == "" or c2 == None:
        return cat_1

    try:
        cat_2 = ProductCategory.objects.get(category_name=c2)
        cat_2.parent_id = cat_1.id
        cat_2.save()
    except:
        return None

    if c3 == "" or c3 == None:
        return cat_2

    try:
        cat_3 = ProductCategory.objects.get(category_name=c3)
        cat_3.parent_id=cat_2.id
        cat_3.save()
        return cat_3
    except:
        return None


def resolve_mul_category(c1, c2, c3):
    if c3 is not None:
        cat_1 = ProductCategory.objects.get(cateogry_name=c1)
        cat_2 = ProductCategory.objects.get(category_name=c2, parent_id=cat_1.id)
        try:
            cat_3 = ProductCategory.objects.get(category_name=c3, parent_id=cat_2.id)
            return cat_3
        except:
            parent = cat_2.id
            resolved_category = create_category(c3, parent)
            return resolved_category

    elif c2 is not None:
        cat_1 = ProductCategory.objects.get(category_name=c1)
        try:
            cat_2 = ProductCategory.objects.get(category_name=c2, parent_id=cat_1.id)
            return cat_2
        except:
            parent = cat_1.id
            resolved_category = create_category(c2, parent)
            return resolved_category


def create_default_top_brands(crop):
    seeds = ProductCategory.objects.get(category_name='Seeds')
    cn = ProductCategory.objects.get(category_name='Crop Nutrition')
    cp = ProductCategory.objects.get(category_name='Crop Protection')
    hw = ProductCategory.objects.get(category_name='Hardware')
    top_brands_seeds, _ = TopBrandsCropCategory.objects.get_or_create(crop=crop, 
                                                                      sub_category=seeds)

    top_brands_cp, _= TopBrandsCropCategory.objects.get_or_create(crop=crop ,
                                                                  sub_category=cp)
    top_brands_cn, _= TopBrandsCropCategory.objects.get_or_create(crop=crop,
                                                                  sub_category=cn)
    top_brands_hw, _= TopBrandsCropCategory.objects.get_or_create( crop = crop, 
                                                                    sub_category=hw )
    logger.info("Top brand created for {}".format(crop.category_name))


def create_category(category_name, parent_id):
    category = ProductCategory.objects.create()
    category.category_name = category_name
    category.parent_id = parent_id
    category.status_id = 1
    category.enable = True
    category.image = '{}.jpg'.format(category_name)
    category.save()
    logger.info("Created {}".format(category_name))
    create_default_top_brands(category)
    return category


def update_category(category, row):
    for language in Language.objects.all():
        cat_desc = category.product_category_descriptions.get( 
                       language__language_code = language.language_code )
        cat_desc.category_name = row[language.language_code]
        cat_desc.save()
    logger.info("Updated descriptions {}".format(row['en']))


@transaction.atomic()
def main(source_file):
    csvfile = open(source_file)
    reader = csv.DictReader(csvfile)

    logger.info("Creating categories...")
    for i, row in enumerate(reader):
        logger.info("{}. row = {}".format(i, row))

        c1 = row['C1'].strip() if row['C1'].strip() != "" else None
        c2 = row['C2'].strip() if row['C2'].strip() != "" else None
        c3 = row['C3'].strip() if row['C3'].strip() != "" else None
        mul = row['Multiple'].strip() if row['Multiple'].strip() != "" else None

        if mul is None:
            resolved_category = resolve_category(c1, c2, c3)
        else:
            resolved_category = resolve_mul_category(c1, c2, c3)
        
        if not resolved_category:
            if c2 is None:
                parent = ProductCategory.objects.get( category_name = 'All' )                
                category_name = c1
            elif c3 is None:
                parent = ProductCategory.objects.get( category_name = c1 )
                category_name = c2
            else:
                grandparent = ProductCategory.objects.get( category_name = c1 )            
                parent = ProductCategory.objects.get( category_name = c2 , parent_id = grandparent.id )
                category_name = c3

            resolved_category = create_category(category_name, parent.id)

        update_category(resolved_category, row)


if __name__ == '__main__':

    source_file = sys.argv[1]
    main(source_file)