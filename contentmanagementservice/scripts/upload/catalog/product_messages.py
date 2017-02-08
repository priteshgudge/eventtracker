import django
import csv
import logging
import sys
django.setup()
from agro_db.catalog_management.models import *
from django.db import transaction

logger = logging.getLogger('main')


def assign_message(display_message, row):
    for language in Language.objects.all():
        msg = display_message.messages.get(
                       language=language)
        msg.text = row[language.language_code]
        msg.save()

    logging.info("Localised messages set.")


def create_display_message(row):
    message_id = row['Message ID'].strip()
    if not message_id:
        raise ValueError("Message ID is empty")

    display_message, created = DisplayMessage.objects.get_or_create(message_code=message_id)
    if created:
        logging.info("Created {}".format(display_message))
    else:
        logging.info("Updated {}".format(display_message))

    return display_message


@transaction.atomic()
def main(source_file):
    csvfile = open(source_file)
    reader = csv.DictReader(csvfile)

    logger.info("Updating Display Messages")
    for i, row in enumerate(reader):
        logger.info("{}. row = {}".format(i, row))

        display_message = create_display_message(row)
        assign_message(display_message, row)

    logging.info("done.")


if __name__ == '__main__':
    source_file = sys.argv[1]
    main(source_file)