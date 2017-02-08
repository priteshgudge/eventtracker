import django

django.setup()
from django.db import transaction
import sys
import csv
import logging
from datetime import datetime
from agro_db.catalog_management.models import Offers, ProductCatalog
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger('main')


def update_applicable_products(product_details, offer_obj):
    products = set(product_details.strip(" ").split(";"))
    if len(products) == 0:
        logger.info("Applicable product is empty for {}".format(offer_obj.offer_code))
        return True
    present_prod = set(offer_obj.applicable_products.all())
    diff = products.difference(present_prod)
    logger.info("diff = {}".format(diff))
    try:
        for prod in diff:
            try:
                product_obj = ProductCatalog.objects.get(sku_code=prod)
            except:
                logger.info("Applicable product not found {}".format(prod))
                return False
            offer_obj.applicable_products.add(product_obj)
        offer_obj.save()
        return True
    except Exception as e:
        logger.info("Error while updating applicable products {}".format(e))
        return False


def create_offer_object(row):
    offer_code = row["offer_code"]
    start_time = datetime.strptime(row["start_time"], "%Y-%m-%d")
    end_time = datetime.strptime(row["end_time"], "%Y-%m-%d")
    primary_product = row["primary_product"]
    applicable_prods = row["applicable_products"]
    priority = row["priority"]
    english_offer_name = row["english_offer_name"]
    hindi_offer_name = row["hindi_offer_name"]
    marathi_offer_name = row["marathi_offer_name"]
    gujrati_offer_name = row["gujrati_offer_name"]
    english_offer_desc = row["english_offer_desc"]
    hindi_offer_desc = row["hindi_offer_desc"]
    marathi_offer_desc = row["marathi_offer_desc"]
    gujrati_offer_desc = row["gujrati_offer_desc"]

    changes = dict(created=0, updated=0)

    try:
        primary_prod = ProductCatalog.objects.get(sku_code=primary_product)
    except:
        primary_prod = ProductCatalog.objects.all()[0]

    try:
        offer_object = Offers.objects.get(offer_code=offer_code)
        changes['updated'] += 1
        logger.info("Updated {}".format(offer_object))
    except ObjectDoesNotExist:
        offer_object = Offers(offer_code=offer_code)
        changes['created'] += 1
        logger.info("Created {}".format(offer_object))
    except Exception as err:
        logger.error(err)
        raise

    offer_object.primary_product = primary_prod
    offer_object.priority = priority
    offer_object.offer_name = english_offer_name
    offer_object.start_time = start_time
    offer_object.end_time = end_time
    offer_object.save()
    status = update_applicable_products(applicable_prods, offer_object)
    if status == False:
        return False

    en_desc = offer_object.offer_descritions.get(language__language_code="en")
    gu_desc = offer_object.offer_descritions.get(language__language_code="gu")
    hi_desc = offer_object.offer_descritions.get(language__language_code="hi")
    mr_desc = offer_object.offer_descritions.get(language__language_code="mr")

    en_desc.offer_name = english_offer_name
    en_desc.offer_description = english_offer_desc
    en_desc.offer_image = offer_code + "_" + en_desc.language.language_code[0].upper() + ".jpg"
    en_desc.save()

    gu_desc.offer_name = gujrati_offer_name
    gu_desc.offer_description = gujrati_offer_desc
    gu_desc.offer_image = offer_code + "_" + gu_desc.language.language_code[0].upper() + ".jpg"
    gu_desc.save()

    hi_desc.offer_name = hindi_offer_name
    hi_desc.offer_description = hindi_offer_desc
    hi_desc.offer_image = offer_code + "_" + hi_desc.language.language_code[0].upper() + ".jpg"
    hi_desc.save()

    mr_desc.offer_name = marathi_offer_name
    mr_desc.offer_description = marathi_offer_desc
    mr_desc.offer_image = offer_code + "_" + mr_desc.language.language_code[0].upper() + ".jpg"
    mr_desc.save()

    offer_object.enable = True
    offer_object.save()

    logger.info("done.")
    return changes


@transaction.atomic()
def main(filename):
    csvfile = open(filename)
    reader = csv.DictReader(csvfile)

    logger.info("Updating app offers...")
    for row in reader:
        logger.info("row = {}".format(row))
        create_offer_object(row)


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
    # TODO: I think once offer management is integrated in catalog,
    # catalog will start consuming offers from offerservice. This script should be removed then.
