# -*- coding: utf-8 -*-

import django

django.setup()
from agro_db.catalog_management.models import *
import csv
import sys
from django.db import transaction
import logging

logger = logging.getLogger('main')


def update_issue(issue, row):
    for language in Language.objects.all():
        issue_desc = issue.crop_issue_descriptions.get(language=language)
        issue_desc.issue_name = row[language.language_code]
        issue_desc.issue_description = row[language.language_code]
        issue_desc.save()
        issue.save()


@transaction.atomic()
def main(sourceFile):
    csvfile = open(sourceFile)
    reader = csv.DictReader(csvfile)

    changes = dict(created=0, updated=0)
    logger.info("Updating issues...")

    for i, row in enumerate(reader):
        logger.info("{}. row = {}".format(i, row))
        issue_map = {
            'CP': 'Crop Protection',
            'CN': 'Crop Nutrition'
        }

        issue_type = ProductCategory.objects.get(category_name=issue_map.get(row["Solution Type"]))
        issue, created = CropIssue.objects.get_or_create(issue_code=row["Issue Code"],issue_type = issue_type)
        if created:
            logger.info("created {}".format(issue))
            changes['created'] += 1
        else:
            logger.info("Updated{}".format(issue))
            changes['updated'] += 1

        issue.issue_name = row['en']
        issue.save()

        update_issue(issue, row)

    logger.info("done")
    return changes


if __name__ == '__main__':
    sourceFile = sys.argv[1]
    main(sourceFile)
