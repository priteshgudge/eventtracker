import django
import csv
import logging
import sys
django.setup()
from agro_db.catalog_management.models import *
from django.db import transaction

logger = logging.getLogger('main')


def whitelist_skus(csv_skus):

    csv_skus = set(csv_skus)
    existing_skus = ProductCatalog.objects.values_list('sku_code', flat=True).filter(sku_code__in=csv_skus)

    non_existing_skus = csv_skus.difference(existing_skus)

    if non_existing_skus:
        raise ValueError("Following Skus are not present in DB{}".format(non_existing_skus))

    product_list = ProductCatalog.objects.filter(sku_code__in=existing_skus)
    whitelist = [StockVisibilityWhiteList(product_sku=product) for product in product_list]

    StockVisibilityWhiteList.objects.bulk_create(whitelist)
    logging.info("done.")


@transaction.atomic()
def main(source_file):

    csvfile = open(source_file)
    reader = csv.DictReader(csvfile)

    logger.info("Updating whitelisted SKUs")

    StockVisibilityWhiteList.objects.all().delete()
    csv_skus = []
    for i, row in enumerate(reader):
        logger.info("{}. row = {}".format(i, row))
        csv_skus.append(row['SKU Code'].strip())

    whitelist_skus(csv_skus)

if __name__ == '__main__':
    source_file = sys.argv[1]
    main(source_file)