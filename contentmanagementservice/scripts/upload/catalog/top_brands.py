# -*- coding: utf-8 -*-

import csv
import logging
import sys

import django
from django.db import transaction

django.setup()

from agro_db.catalog_management.models import *

logger = logging.getLogger('main')


def get_brands_from_names(brand_names):
    brand_names = map(lambda x: x.strip(), brand_names.split(","))
    brand_objects = []
    for t in brand_names:
        try:
            brand_objects.append(ProductBrand.objects.get(brand_name=t))
        except:
            print "Brand not found : ", t
    return brand_objects


@transaction.atomic()
def main(source_file):
    csvfile = open(source_file)
    reader = csv.DictReader(csvfile)

    seeds = ProductCategory.objects.get(category_name='Seeds')
    cn = ProductCategory.objects.get(category_name='Crop Nutrition')
    cp = ProductCategory.objects.get(category_name='Crop Protection')
    hw = ProductCategory.objects.get(category_name='Hardware')

    logger.info("Updating top brands...")

    for row in reader:
        logger.info("row = {}".format(row))

        crop = ProductCategory.objects.get(category_name=row['Crop'])
        seeds_brands = get_brands_from_names(row['Seeds'])
        cp_brands = get_brands_from_names(row['CP'])
        cn_brands = get_brands_from_names(row['CN'])
        hardware_brands = get_brands_from_names(row['HW'])

        top_brands_seeds, _ = TopBrandsCropCategory.objects.get_or_create(crop=crop, sub_category=seeds)

        top_brands_cp, _ = TopBrandsCropCategory.objects.get_or_create(crop=crop, sub_category=cp)

        top_brands_cn, _ = TopBrandsCropCategory.objects.get_or_create(crop=crop, sub_category=cn)

        top_brands_hw, _ = TopBrandsCropCategory.objects.get_or_create(crop=crop, sub_category=hw)

        for t in seeds_brands:
            if t not in top_brands_seeds.top_brands.all():
                top_brands_seeds.top_brands.add(t)
        top_brands_seeds.save()

        for t in cp_brands:
            if t not in top_brands_cp.top_brands.all():
                top_brands_cp.top_brands.add(t)
        top_brands_cp.save()

        for t in cn_brands:
            if t not in top_brands_cn.top_brands.all():
                top_brands_cn.top_brands.add(t)
        top_brands_cn.save()

        for t in hardware_brands:
            if t not in top_brands_hw.top_brands.all():
                top_brands_hw.top_brands.add(t)
        top_brands_hw.save()

    logger.info("done.")


if __name__ == "__main__":
    source_file = sys.argv[1]
    main(source_file)
