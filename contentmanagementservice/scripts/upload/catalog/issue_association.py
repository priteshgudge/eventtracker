# -*- coding: utf-8 -*-
import sys
import django
django.setup()
from agro_db.catalog_management.models import *
from django.db import transaction

import logging

logger = logging.getLogger('main')

category_map = {"CP": ProductCategory.objects.get(category_name="Crop Protection"),
                "CN": ProductCategory.objects.get(category_name="Crop Nutrition")}


def validate_issue_skus(content,label_map):

    csv_skus = set()
    data = map(lambda row: row[:-1].split(','), content)[1:]

    for i, row in enumerate(data):
        csv_skus.update(filter(lambda x: True if x.strip() != "" else False, row[label_map["Solution Products"]:]))

    existing_skus = set(ProductCatalog.objects.values_list('sku_code', flat=True).filter(sku_code__in=csv_skus))

    difference = csv_skus.difference(existing_skus)

    if difference:
        raise ValueError("Following Skus are not present in DB{}".format(difference))

@transaction.atomic()
def main(sourceFile):
    with open(sourceFile) as f:
        content = f.readlines()

        label_map = {
            "Disease Code": 0,
            "Issue Reference": 1,
            "Crop": 2,
            "Disease Name": 3,
            "Disease Name Gujarati": 4,
            "Disease Name Hindi": 5,
            "Disease Name Marathi": 6,
            "Description": 7,
            "Description Gujarati": 8,
            "Description Hindi": 9,
            "Description Marathi": 10,
            "Solution Products": 11
        }

    validate_issue_skus(content, label_map)

    data = map(lambda row: row[:-1].split(','), content)[1:]
    logger.info("Updating Diseases...")
    for i, row in enumerate(data):
        logger.info("{}. row = {}".format(i, row))
        crop_obj = ProductCategory.objects.get(category_name=row[label_map["Crop"]])
        issue,_ = CropIssue.objects.get_or_create(issue_code=row[label_map["Issue Reference"]])

        disease_english = row[label_map["Disease Name"]]
        disease_gujrati = row[label_map["Disease Name Gujarati"]]
        disease_marathi = row[label_map["Disease Name Marathi"]]
        disease_hindi = row[label_map["Disease Name Hindi"]]

        description_english = row[label_map["Description"]]
        description_gujrati = row[label_map["Description Gujarati"]]
        description_marathi = row[label_map["Description Marathi"]]
        description_hindi = row[label_map["Description Hindi"]]
        disease, _ = CropIssueAssociation.objects.get_or_create(disease_code=row[label_map["Disease Code"]],
                                                                crop=crop_obj, crop_issue=issue)
        disease.issue_association_image = disease.disease_code + ".jpg"

        en_desc = disease.association_descriptions.get(language__language_code='en')
        gu_desc = disease.association_descriptions.get(language__language_code='gu')
        mr_desc = disease.association_descriptions.get(language__language_code='mr')
        hi_desc = disease.association_descriptions.get(language__language_code='hi')

        en_desc.crop_issue_disease = disease_english
        en_desc.crop_issue_description = description_english
        en_desc.save()

        mr_desc.crop_issue_disease = disease_marathi
        mr_desc.crop_issue_description = description_marathi
        mr_desc.save()

        hi_desc.crop_issue_disease = disease_hindi
        hi_desc.crop_issue_description = description_hindi
        hi_desc.save()

        gu_desc.crop_issue_disease = disease_gujrati
        gu_desc.crop_issue_description = description_gujrati
        gu_desc.save()

        products = set(filter(lambda x: True if x.strip() != "" else False, row[label_map["Solution Products"]:]))
        existig_prod = set(x.sku_code for x in disease.solutions.all())
        difference = existig_prod.difference(products)

        logger.debug("difference = {}".format(difference))
        for prod in difference:
            p = ProductCatalog.objects.get(sku_code=prod)
            disease.solutions.remove(p)

        for product in products:
            p = ProductCatalog.objects.get(sku_code=product)
            if p not in disease.solutions.all():
                disease.solutions.add(p)
        disease.save()

    logger.info("done.")


if __name__ == '__main__':
    sourceFile = sys.argv[1]
    main(sourceFile)
