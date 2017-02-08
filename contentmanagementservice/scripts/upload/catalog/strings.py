import csv
import sys
import logging
import django

django.setup()

from agro_db.catalog_management.models import CatalogStrings, Language
from django.db import transaction

logger = logging.getLogger('main')


def create_json(row):
    result = {"string": row["string"],
              "desc": [{"language": l.language_code, "string": row[l.language_code]} for l in Language.objects.all()]}
    return result


def populate_string(desc, obj):
    lang_map = {x.language.language_code: x for x in obj.descriptions.all()}
    desc = desc["desc"]
    for d in desc:
        obj = lang_map[d.get("language")]
        obj.description = d["string"]
        obj.save()


@transaction.atomic()
def main(source_file):
    csvfile = open(source_file)
    reader = csv.DictReader(csvfile)

    changes = dict(created=0, updated=0)
    logger.info("Updating Strings...")

    for row in reader:
        logger.info("row = {}".format(row))
        obj, created = CatalogStrings.objects.get_or_create(string_code=row["string"])
        if created:
            logger.info("Created {}".format(obj))
            changes['created'] += 1
        else:
            logger.info("Updated {}".format(obj))
            changes['updated'] += 1
        response_json = create_json(row)
        populate_string(response_json, obj)

    logger.info("done")
    return changes


if __name__ == "__main__":
    source_file = sys.argv[1]
    main(source_file)
