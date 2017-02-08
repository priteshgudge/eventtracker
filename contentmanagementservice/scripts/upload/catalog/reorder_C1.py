# -*- coding: utf-8 -*-

import sys
import csv
import logging
import django
django.setup()
from django.db import transaction
import copy

from catalogservicev2.utils.category_functions import validate_categories
from agro_db.catalog_management.models import Month, Location, ProductCategory, CropCategoryOrder
from catalogservicev2.utils.reordering import DuplicateRankError, InvalidCategoryError

logger = logging.getLogger('main')


def update_crop_category_ranks(month_str, location_str, category_name, category_rank_map):
    logger.debug("Updating ranks for month={}, location={} and crop={}".format(month_str, location_str, category_name))
    logger.debug("Category Ranks={}".format(category_rank_map))

    month, _ = Month.objects.get_or_create(month=month_str)
    location, _ = Location.objects.get_or_create(location=location_str)

    for crop_str, rank in category_rank_map.iteritems():
        logger.debug("Category={}, rank={}".format(crop_str, rank))
        crop = ProductCategory.objects.get(category_name=crop_str)
        category = ProductCategory.objects.get(category_name=category_name)
        crop_category_order, created = CropCategoryOrder.objects.get_or_create(crop_id=crop.id,
                                                                               category_id=category.id,
                                                                               month_id=month.id,
                                                                               location_id=location.id)
        crop_category_order.rank = rank or None
        if created:
            logger.info("Created {}".format(crop_category_order))
        else:
            logger.info("Updated {}".format(crop_category_order))

        crop_category_order.save()


@transaction.atomic()
def main(source_file):
    logger.info("Reordering C1...")
    with open(source_file, 'r') as csv_file:
        dict_reader = csv.DictReader(csv_file)
        categories = copy.deepcopy(dict_reader.fieldnames)
        categories.remove('Month')
        categories.remove('State')
        categories.remove('Type')
        validate_categories(categories)
        for line in dict_reader:
            try:
                update_crop_category_ranks(month_str=line.pop('Month'), location_str=line.pop('State'), category_name=line.pop('Type'), category_rank_map=line)
            except DuplicateRankError as err:
                logger.error(err)
                continue

    logger.info("Done!")

if __name__ == '__main__':
    source_file = sys.argv[1]
    main(source_file)
