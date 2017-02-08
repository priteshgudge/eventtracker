# -*- coding: utf-8 -*-

import sys
import csv
import copy
import logging
from django.db import transaction
import django
django.setup()

from catalogservicev2.utils.category_functions import validate_categories
from catalogservicev2.utils.reordering import DuplicateRankError, InvalidCategoryError
from agro_db.catalog_management.models import Month, Location, ProductCategory, CategoryOrder

logger = logging.getLogger('main')


def update_category_ranks(month_str, location_str, category_rank_map):
    logger.debug("Updating ranks for month={}, location={}".format(month_str, location_str))
    logger.debug("Crop Ranks={}".format(category_rank_map))

    month, _ = Month.objects.get_or_create(month=month_str)
    location, _ = Location.objects.get_or_create(location=location_str)

    for category, rank in category_rank_map.iteritems():
        logger.debug("Category={} and rank={}".format(category, rank))
        category = ProductCategory.objects.get(category_name=category)
        crop_order, created = CategoryOrder.objects.get_or_create(category_id=category.id, month_id=month.id,
                                                                  location_id=location.id)
        crop_order.rank = rank or None
        if created:
            logger.info("Created {}".format(crop_order))
        else:
            logger.info("Updated {}".format(crop_order))

        crop_order.save()


@transaction.atomic()
def main(source_file):
    with open(source_file, 'r') as csv_file:
        dict_reader = csv.DictReader(csv_file)
        categories = copy.deepcopy(dict_reader.fieldnames)
        categories.remove('Month')
        categories.remove('State')
        validate_categories(categories)
        for line in dict_reader:
            try:
                update_category_ranks(month_str=line.pop('Month'), location_str=line.pop('State'), category_rank_map=line)
            except DuplicateRankError as err:
                logger.error(err)
                continue

    logger.info("Done!")


if __name__ == '__main__':
    source_file = sys.argv[1]
    main(source_file)
