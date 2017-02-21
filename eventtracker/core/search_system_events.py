import ast
import json
import logging
import pymongo
from bson import ObjectId
from bson.dbref import DBRef
from datetime import datetime

from eventtracker.utils.encoder import BsonToJsonEncoder
from eventtracker.utils.validation import LANGUAGES
from agroutils.exceptions.agro_error import AgroError
from flask import current_app as app

logger = logging.getLogger('main')

def search_system_events(**kwargs):
    """
    :param kwargs:
    include: ids to include in response
    entityType : type of object notification was sent for ['order','farmer','ticket','product']
    entityId: name : entity id of object notification was sent on
    eventType: type of notification : [sms,email]
    eventName: name of events: [order_edit_sms etc]
    searchDict: optional key,values {farmerId, orderId, ticketId}
    timestamp: (ts1): from timestamp, (ts1,ts2) To timestamp
    sortBy: list of tuples {default: timestamp: Descending}  else sort([("field1",pymongo.ASCENDING), ("field2",pymongo.DESCENDING)])
    exclude: ids to exclude from search
    projection: dict of projection
    transform : bson to json encoding
    :return:list of events
    """
    #config = get_config_object()
    #client_url = app.config.get('MONGO_DB_URI', "mongodb://localhost:17017/")
    # FOR TEST
    client = kwargs.get('client')
    client = app.db_client
    if not client:
        client_url = "mongodb://localhost:17017/"
        client = pymongo.MongoClient(client_url)
    #db = client.system_events
    # For test
    db = client.system_events_test
    logger.info("search Events :: {}".format(locals().copy()))

    cursor = db.events

    #language = kwargs.get('language', 'en') or 'en'
    #assert language in LANGUAGES, "Invalid language '{}'".format(language)

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

    # Filter according to entityType
    type_param = kwargs.get('entityType')
    if type_param:
        query.update({'entityType': type_param})
        entity_id = kwargs.get('entityId')
        if entity_id:
            if isinstance(entity_id, list):
                query.update({'entityId': {'$in': entity_id}})
            else:
                query.update({'entityId': entity_id})

    # Filter According to event Type
    event_type = kwargs.get('eventType')
    if event_type:
        if isinstance('eventType', list):
            query.update({'eventType': {'$in' : event_type}})
        else:
            query.update({'eventType': event_type})
            event_name = kwargs.get('eventName')
            if event_name:
                query.update({'eventName': event_name})

    # Filter According to timestamp
    timestamp = kwargs.get('timestamp')
    if timestamp:
        if isinstance(timestamp,tuple):
            tquery = {'timestamp': {'$gte': timestamp[0], '$lte': timestamp[1]}}
        else:
            tquery = { 'timestamp': {'$gte': timestamp}}

        query.update(tquery)

    search_keys_dict = kwargs.get('searchDict')
    if search_keys_dict:
        query.update(search_keys_dict)

    if projection:
        cursor = cursor.find(query, projection)
    else:
        cursor = cursor.find(query)

    sort_by = kwargs.get('sortBy')
    if not sort_by:
        cursor = cursor.sort('timestamp',pymongo.DESCENDING)
    else:
        cursor = cursor.sort(sort_by)

    if 'offset' in kwargs.keys():
        cursor = cursor.skip(kwargs['offset'])
    if 'limit' in kwargs.keys():
        cursor = cursor.limit(kwargs['limit'])
    print query, projection
    total = cursor.count(with_limit_and_skip=True)

    event_list = []

    #for event in cursor:
    #    if transform:
    #        transformed = transform_event(event)
    #        event_list.append(transformed)
    if transform:
        event_list = [transform_event(event) for event in cursor]
    else:
        event_list = [event for event in cursor]
    return event_list

def transform_event(template):

    template.pop('_id')
    template_dict = json.loads(json.dumps(template, cls=BsonToJsonEncoder))
    return template_dict