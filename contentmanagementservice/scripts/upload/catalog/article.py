# -*- coding: utf-8 -*-

import csv
import logging
import json
from pymongo import MongoClient

from contentmanagementservice.utils.encoder import BsonToJsonEncoder
from contentmanagementservice.utils.config import get_config_object

config = get_config_object()
client = MongoClient()
db = client.content
logger = logging.getLogger('main')


def put_articles(article_list):
    logger.info("Upserting all articles in bulk")
    collection = db.articles
    bulk = collection.initialize_unordered_bulk_op()
    for article in article_list:
        bulk.find({'code': article['code']}).upsert().update({'$set': article})

    result = bulk.execute()

    result = json.loads(json.dumps(result, cls=BsonToJsonEncoder))
    logger.info("Upsert response {}".format(result))

    return result


def formulate_article_tags(row):
    article_tags = []
    tags = row['tags'].split(',')
    english_tags = row['english_tags'].split(',')
    gujrati_tags = row['gujrati_tags'].split(',')
    hindi_tags = row['hindi_tags'].split(',')
    marathi_tags = row['marathi_tags'].split(',')
    for i, t in enumerate(tags):
        tag = dict(
            code=t.strip(),
            descriptions=dict(
                en=dict(heading=english_tags[i].strip()),
                gu=dict(heading=gujrati_tags[i].strip()),
                hi=dict(heading=hindi_tags[i].strip()),
                mr=dict(heading=marathi_tags[i].strip())
            )
        )
        article_tags.append(tag)
    return article_tags


def _media_item(media):
    """
    Every media is like "media_name;media_type"
    :return: dict(url of media, type of media)
    """
    _url, _type = [m.strip() for m in media.split(';')[:2]]
    # Just didn't want to clash the reserved keywords, so used _
    if _type == 'image':
        return dict(url='{}{}.jpg'.format(config.IMAGES_API_REFERENCE, _url), type=_type)

    return dict(url=_url, type=_type)


def main(source_file):
    csvfile = open(source_file)
    reader = csv.DictReader(csvfile)

    article_list = []
    logger.info("Updating articles...")
    for i, row in enumerate(reader):
        logger.info("{}. row = {}".format(i, row))
        article = dict(
            code=row['article_code'],
            date=row['date'],
            descriptions=dict(
                en=dict(
                    heading=row['english_heading'],
                    description=row['english_description'],
                    farmer_name=row['english_farmer_name'],
                    synopsis=row['english_synopsis'],
                    address_location=row['english_address_location'],
                    media=[_media_item(media) for media in row['english_media'].split(',')]
                ),
                gu=dict(
                    heading=row['gujrati_heading'],
                    description=row['gujrati_description'],
                    farmer_name=row['gujrati_farmer_name'],
                    synopsis=row['gujrati_synopsis'],
                    address_location=row['gujrati_address_location'],
                    media=[_media_item(media) for media in row['gujrati_media'].split(',')]
                ),
                hi=dict(
                    heading=row['hindi_heading'],
                    description=row['hindi_description'],
                    farmer_name=row['hindi_farmer_name'],
                    synopsis=row['hindi_synopsis'],
                    address_location=row['hindi_address_location'],
                    media=[_media_item(media) for media in row['hindi_media'].split(',')]
                ),
                mr=dict(
                    heading=row['marathi_heading'],
                    description=row['marathi_description'],
                    farmer_name=row['marathi_farmer_name'],
                    synopsis=row['marathi_synopsis'],
                    address_location=row['marathi_address_location'],
                    media=[_media_item(media) for media in row['marathi_media'].split(',')],
                ),
            ),
            source=dict(
                code=row['source'],
                descriptions=dict(
                    en=dict(heading=row['english_source']),
                    gu=dict(heading=row['gujrati_source']),
                    hi=dict(heading=row['hindi_source']),
                    mr=dict(heading=row['marathi_source'])
                )
            ),
            type=dict(
                code=row['type'],
                image='{}{}.jpg'.format(config.IMAGES_API_REFERENCE, row['type']),
                descriptions=dict(
                    en=dict(heading=row['english_type']),
                    gu=dict(heading=row['gujrati_type']),
                    hi=dict(heading=row['hindi_type']),
                    mr=dict(heading=row['marathi_type'])
                )
            ),
            tags=formulate_article_tags(row)
        )
        # NOTE _id is already ObjectId here
        article_list.append(article)

    return put_articles(article_list)