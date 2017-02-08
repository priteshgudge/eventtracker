# -*- coding: utf-8 -*-

import django

django.setup()
from django.db import transaction
from agro_db.catalog_management.models import *
import csv
import sys
import logging

logger = logging.getLogger('main')


def update_attribute(attribute, row):
    for language in Language.objects.all():
        if not language.language_code in row:
            logger.debug("{} language not in row".format(language.language_code))
            continue

        attr_lable = attribute.product_attribute_lables.get(language=language)
        attr_lable.lable = row[language.language_code]
        attr_lable.save()


@transaction.atomic()
def main(sourceFile):
    csvfile = open(sourceFile)
    reader = csv.DictReader(csvfile)

    changes = dict(updated=0, created=0)

    for i, row in enumerate(reader):
        logger.info("{}. row = {}".format(i, row))
        try:
            attribute = ProductAttributeKey.objects.get(attribute_name=row['en'])
            changes['updated'] += 1
            logger.debug("attribute updated")
        except:
            attribute = ProductAttributeKey.objects.create(attribute_name=row['en'])
            changes['created'] += 1
            logger.debug("attribute created")

        category = ProductCategory.objects.get(category_name=row['Category'])
        attr_assoc, _ = ProductCategoryAttributeAssociation.objects.get_or_create(category=category,
                                                                                  product_attribute_key=attribute)

        update_attribute(attribute, row)

    return changes


if __name__ == '__main__':
    sourceFile = sys.argv[1]
    main(sourceFile)
