# -*- coding: utf-8 -*-
import django

django.setup()
from django.db import transaction
from agro_db.catalog_management.models import *
import csv
import sys
import logging

logger = logging.getLogger('main')


def update_brand_descriptions(brand, row):
    for language in Language.objects.all():
        brand_desc = brand.product_brand_desciptions.get(language=language)
        brand_desc.brand_name = row[language.language_code]
        brand_desc.save()
    logger.debug("Brand description updated")


@transaction.atomic()
def main(source_file):
    csvfile = open(source_file)
    reader = csv.DictReader(csvfile)

    changes = dict(updated=0, created=0, errors=0)

    logger.info("Updating brands...")
    for i, row in enumerate(reader):
        logging.info("{}. row = {}".format(i, row))
        brand, created = ProductBrand.objects.get_or_create(brand_name=row['en'])
        if created:
            changes['created'] += 1
            logger.info("created brand {}".format(brand))
        else:
            changes['updated'] += 1
            logger.info("updating brand {}".format(brand))
        brand.enable = True
        brand.brand_image = '{}.jpg'.format(row['en'])
        brand.priority = row["priority"]
        brand.save()
        update_brand_descriptions(brand, row)

    logger.info("done")
    return changes


if __name__ == '__main__':
    source_file = sys.argv[1]
    main(source_file)
