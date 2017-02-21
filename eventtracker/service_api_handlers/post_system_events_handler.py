import ast
import json
import logging
import pymongo
import traceback
from bson import ObjectId
from bson.dbref import DBRef
from datetime import datetime
from agroutils.exceptions.agro_error import AgroError
from flask import current_app as app


from eventtracker.utils.encoder import BsonToJsonEncoder
from eventtracker.utils.validation import LANGUAGES
from eventtracker.utils.validation import  validate_system_event_request, validate_system_event_list
logger = logging.getLogger('main')



def get_system_event_collection_cursor():
    #config = get_config_object()

    try:
        client_url = app.config.get('MONGO_DB_URI', "mongodb://localhost:17017/")
        # FOR TEST
        # client_url = "mongodb://localhost:17017/"
        client = pymongo.MongoClient(client_url)
        db = client.system_events_test
        cursor = db.events
    except:
        logger.error("Error while connecting to MONGODB" + traceback.format_exc())
        raise AgroError(500, "Error connecting to DB")
    return cursor

def insert_system_event(event_json):
    """

    :param event_json:
        entityType
        entityId
        eventType
        eventName

        other keys: farmerId, orderId, productUUID, ticketUUID,
            --> for search indexing --> sparse indexes
    :return: True or Error
    """
    logger.info("Insert System Event :: {}".format(locals().copy()))
    cursor = get_system_event_collection_cursor()

    try:
        result = cursor.insert_one(event_json)
    except:
        result = None

    if result:
        return True
    else:
        raise AgroError(422, "Record action for system event failed")


def post_system_event(request_details):

    validate_system_event_request(request_details)

    if 'event' in request_details:
        insertion = insert_system_event(request_details['event'])
    else:
        raise AgroError(501, "Not implemented for your request")

    return {},201