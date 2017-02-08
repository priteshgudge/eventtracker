import ast
import json
import logging
import pymongo
from bson import ObjectId
from bson.dbref import DBRef
from datetime import datetime

from contentmanagementservice.utils.encoder import BsonToJsonEncoder
from contentmanagementservice.utils.validation import LANGUAGES, DocumentError
from contentmanagementservice.utils.config import get_config_object

from contentmanagementservice.core.template_constants import (ORDER_CANCEL_HTML,
                                                              ORDER_CREATE_HTML,ORDER_EDIT_HTML)
from contentmanagementservice.utils.logger import get_main_logger
from agroutils.exceptions.agro_error import AgroError
from flask import current_app as app

logger = logging.getLogger('main')

def search_template(**kwargs):
    """

    :param kwargs:
    include: ids to include in response
    type : type of articles sms, email: if type is empty search with name
    name : name of articles : if name is empty search with type
            If both name and type search on both
    exclude: ids to exclude from search
    projection: dict of projection
    transform : bson to json encoding
    :return:list of articles
    """
    #config = get_config_object()
    client_url = app.config.get('MONGO_DB_URI', "mongodb://localhost:27017/")
    # FOR TEST
    # client_url = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(client_url)
    db = client.notification_templates
    logger.info("search template :: {}".format(locals().copy()))

    cursor = db.templates

    language = kwargs.get('language', 'en') or 'en'
    assert language in LANGUAGES, "Invalid language '{}'".format(language)

    projection = kwargs.get('projection', {}) or {}
    transform = kwargs.get('transform', True)

    query = dict()

    # Exclude id in list
    exclude = kwargs.get('exclude')
    if exclude and isinstance(exclude, list):
        query.update({'_id': {'$nin': map(ObjectId, exclude)}})

    # Include ID in list
    include = kwargs.get('include')
    if isinstance(include, list):
        query.update({'_id': {'$in': map(ObjectId, include)}})

    # Filter according to type
    type_param = kwargs.get('type')
    if type_param:
        query.update({'type': type_param})

    # Filter according to name & second level language
    name = kwargs.get('name')
    if name:
        query.update({'name': name})

    if language:
        query.update({'language': language})

    if projection:
        cursor = cursor.find(query, projection)
    else:
        cursor = cursor.find(query)

    total = cursor.count()

    template_list = []

    for template in cursor:
        if transform:
            transformed = transform_template(template)
            template_list.append(transformed)

    return template_list

def transform_template(template):

    template.pop('_id')
    template_dict = json.loads(json.dumps(template, cls=BsonToJsonEncoder))
    return template_dict

def get_template_string(template_type, template_name, language="en"):

    template_list = search_template(name=template_name, type=template_type, language=language)
    if template_list:
        template = template_list[0]
    else:
        template = {}
    return template

def get_template(params):
    try:
        template_type = params['type'].lower()
        template_name = params['name'].upper()
        template_language = params.get('language','en')
    except:
        raise AgroError(400, "Bad Request Parameters")

    template_dict = get_template_string(template_type, template_name, template_language)

    if not template_dict:
        raise AgroError(404, "Matching Template Not Found")

    try:
        template_subject = template_dict.get('subject')
        template = template_dict['body']
        fields = template_dict.get('fields', [])
    except:
        raise AgroError(422, "Error in template object")

    return dict(name=template_name, type=template_type, body=template, subject=template_subject,fields=fields)


if __name__== "__main__":
    params = dict(type="email",name="ORDERCREATE")
    result = get_template(params)
    print result