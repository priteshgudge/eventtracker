# -*- coding: utf-8 -*-

import django

django.setup()
import csv
import sys
import logging
from django.db import transaction
from agro_db.catalog_management.models import *

logger = logging.getLogger('main')


def update_manufacturer(manufacturer, row):
    for language in Language.objects.all():
        if not language.language_code in row:
            continue

        man_desc = manufacturer.product_manufacturer_descriptions.get(language=language)
        man_desc.brand_name = row[language.language_code]
        man_desc.save()


@transaction.atomic()
def main(sourceFile):
    csvfile = open(sourceFile)
    reader = csv.DictReader(csvfile)

    changes = dict(created=0, updated=0)

    logger.info("Updating Manufacturer...")
    for i, row in enumerate(reader):
        logger.info("{}. row = {}".format(i, row))
        manufacturer, created = ProductManufacturer.objects.get_or_create(product_manufacturer=row['en'])
        if created:
            changes['created'] += 1
            logger.info("created {}".format(manufacturer))
        else:
            changes['updated'] += 1
            logger.info("updated {}".format(manufacturer))

        update_manufacturer(manufacturer, row)

    logger.info("done.")
    return changes


if __name__ == '__main__':
    sourceFile = sys.argv[1]
    main(sourceFile)
