# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
from bson import ObjectId


entity_type_set = set(['order','ticket','farmer','product'])
event_type_set = set(['sms','email'])
event_name_set = set(['order_create_sms','order_edit_sms','order_cancel_sms',
                        'order_create_email','order_edit_email','order_cancel_email'
                       'ticket_create_sms','ticket_close_sms','ticket_status_change_sms'])


def create_collection_indexes(db):
    """
    Creates indexes on notifications collections of system_events database
    https://docs.mongodb.com/v3.0/core/index-intersection/ Optimized for index intersection
    :param db:
    :return: db
    """
    result = db.events.create_index([('entityType', pymongo.ASCENDING),('entityId',pymongo.ASCENDING)])
    result = db.events.create_index([('eventType', pymongo.ASCENDING)])
    result = db.events.create_index([('eventName',pymongo.ASCENDING)])
    result = db.events.create_index([('farmerId',pymongo.ASCENDING)], sparse=True)
    result = db.events.create_index([('orderId', pymongo.ASCENDING)], sparse=True)
    result = db.events.create_index([('ticketId', pymongo.ASCENDING)], sparse=True)
    result = db.events.create_index([('timestamp', pymongo.DESCENDING)])
    return db


def create_system_events_database():
    client = MongoClient('localhost', 17017)
    try:
        client.drop_database("system_events")
    except:
        print "Exception while dropping database"
    db = client.system_events
    return db

def get_system_events_database():
    client = MongoClient('localhost', 17017)
    db = client.system_events
    return db

def reindex__system_events_collection(db):
    result = db.events.reindex()
    print "Reindex Operation", result

    return result



if __name__ == '__main__':
    db = create_system_events_database()
    #db = get_system_events_database()
    #result = create_collection_indexes(db)
