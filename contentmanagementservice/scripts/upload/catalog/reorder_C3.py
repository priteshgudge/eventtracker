# -*- coding: utf-8 -*-

import sys
import csv
import logging
import copy
from django.db import transaction
import django
django.setup()

from agro_db.catalog_management.models import CropOrder, Month, Location, ProductCategory
from catalogservicev2.utils.reordering import DuplicateRankError, InvalidCategoryError
from catalogservicev2.utils.category_functions import validate_categories

logger = logging.getLogger('main')


def update_crop_ranks(month_str, location_str, crop_rank_map):
    logger.debug("Updating ranks for month={}, location={}".format(month_str, location_str))
    validate_categories(crop_rank_map)
    ranks_list = crop_rank_map.values()
    rank_set = set(crop_rank_map.values())
    if not len(rank_set) == len(ranks_list):
        raise DuplicateRankError("Duplicate rank for {} & {}".format(month_str, location_str))

    month, _ = Month.objects.get_or_create(month=month_str)
    location, _ = Location.objects.get_or_create(location=location_str)

    for crop, rank in crop_rank_map.iteritems():
        logger.debug("Crop={} and rank={}".format(crop, rank))
        crop = ProductCategory.objects.get(category_name=crop)
        crop_order, created = CropOrder.objects.get_or_create(crop_id=crop.id, month_id=month.id,
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
                update_crop_ranks(month_str=line.pop('Month'), location_str=line.pop('State'), crop_rank_map=line)
            except DuplicateRankError as err:
                logger.error(err)
                continue

    logger.info("Done!")


if __name__ == '__main__':
    source_file = sys.argv[1]
    main(source_file)
