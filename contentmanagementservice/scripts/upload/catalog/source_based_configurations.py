import django
import csv
import logging
import sys
django.setup()

from django.db import transaction
from agro_db.catalog_management.models import *

logger = logging.getLogger('main')


def update_product_source_association(row):
    custom_message = None
    custom_message_text = row['Custom Message'].strip()
    if custom_message_text:
        custom_message = DisplayMessage.objects.get(message_code=custom_message_text)
    product_catalog = ProductCatalog.objects.get(sku_code=row['SKU Code'].strip())
    source = Source.objects.get(source_code=row['Source'].strip())

    association, created = ProductSourceAssociation.objects.get_or_create(product=product_catalog, applicable_source=source)
    association.display_message = custom_message
    association.display_price = ((row['Price Visibility'].strip().lower() or 'y') == 'y')
    association.buy_bar = ((row['Buy Bar Visibility'].strip().lower() or 'y') == 'y')
    association.free_shipping = ((row['Free Shipping'].strip().lower() or 'y') == 'y')
    if (product_catalog.mrp == 0 or product_catalog.selling_price == 0) and association.display_price:
        logger.info("MRP={} or SellingPrice={} for {}. Setting display_price=False".format(
            product_catalog.mrp, product_catalog.selling_price, product_catalog.sku_code))
        association.display_price = False
    association.save()
    if created:
        logger.info("Created {}".format(association))
    else:
        logger.info("Updated {}".format(association))


@transaction.atomic()
def main(source_file):
    csvfile = open(source_file)
    reader = csv.DictReader(csvfile)

    logger.info("Updating Buy Bar, Price Visibility, Shipping Visibility and Product Message")
    for i, row in enumerate(reader):
        logger.info("{}. row = {}".format(i, row))
        update_product_source_association(row)

    logger.info("done.")


if __name__ == '__main__':
    source_file = sys.argv[1]
    main(source_file)