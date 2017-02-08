import sys
import logging
import django

django.setup()

from agro_db.catalog_management.models import *
from django.db import transaction

logger = logging.getLogger('main')


@transaction.atomic()
def main(source_file):
    with open(source_file) as f:
        content = f.readlines()

    data = map(lambda row: row[:-1].split(','), content)[1:]

    logger.info("Updating related products ...")

    for row in data:
        logger.info("row = {}".format(row))
        primary_sku = row[2]
        related_skus = filter(lambda x: True if x.strip() != "" else False, row[3:])

        logger.info("primary sku = {} and related skus = {}".format(primary_sku, related_skus))

        product = ProductCatalog.objects.get(sku_code=primary_sku)

        for t in related_skus:
            related_product = ProductCatalog.objects.get(sku_code=t)
            product.related_products.add(related_product)
            product.save()

    logger.info("done.")


if __name__ == "__main__":
    file_name = sys.argv[1]
    main(file_name)
