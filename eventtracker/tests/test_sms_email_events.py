from eventtracker.scripts.init_system_events_db import create_collection_indexes, reindex__system_events_collection
from eventtracker.core.search_system_events import search_system_events
import pymongo
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime as dt
import random
import uuid
from loremipsum import generate_paragraph
from eventtracker.utils.validation import validate_system_event_request
import time
entity_type_set = set({'order','ticket','farmer','product'})
event_type_set = set({'sms','email'})
event_name_set = set({'order_create_sms','order_edit_sms','order_cancel_sms',
                        'order_create_email','order_edit_email','order_cancel_email',
                       'ticket_create_sms','ticket_close_sms','ticket_status_change_sms'})


client_url = "mongodb://localhost:17017/"
client = None

epoch = dt.utcfromtimestamp(0)

def unix_time_millis(dt):
    #return int((dt - epoch).total_seconds() * 1000)
    return int(dt.strftime("%s")) * 1000
def create_temp_database():
    #client = MongoClient('localhost', 17017)
    try:
        client.drop_database("system_events_test")
    except:
        print "Exception while dropping database"
    db = client.system_events_test
    #create_collection_indexes(db)
    return db

def generate_sms_random():
    timestamp = unix_time_millis(dt.now())
    event_type = random.choice(list(event_type_set))
    entity_type = random.choice(list(entity_type_set))
    entity_id = str(random.randint(a=10000, b=99999))
    event_name_list = filter(lambda x: event_type in x and entity_type in x,event_name_set)
    farmer_id = str(random.randint(10001,10003))

    if event_name_list:
        event_name = random.choice(event_name_list)
    else:
        event_name = "order_create_email"
    a,b,c = generate_paragraph()
    event_details = dict(info="a", info_id='b', first=a,second=b, text=c)

    event_dict = dict(eventType='sms', eventName=event_name, entityType=entity_type, entityId=entity_id,
                      eventDetails=event_details, timestamp=timestamp, farmerId=farmer_id)

    return event_dict

def insert_sms_event(db, event_dict):

    validate_system_event_request(dict(event=event_dict))
    result = db.events.insert_one(event_dict)
    #print result, event_dict

def generate_multiple_events(num=100):
    event_list = []
    for i in range(num):
        event =   generate_sms_random()
        event_list.append(event)
    return event_list

def insert_multiple_sms(db, event_list):
    for ev in event_list:
        insert_sms_event(db,ev)

def get_test_db():
    client = MongoClient('localhost', 17017)

    db = client.system_events_test
    return db

def read_func():
    global client
    time1 = time.time()
    #    insert_multiple_sms(db, ev_list)
    time2 = time.time()
    print '%s function took %0.5f ms' % ('write entries mongo with validation', (time2 - time1) * 1000.0)

    db = get_test_db()

    #    reindex__system_events_collection(db)

    time1 = time.time()
    lst = search_system_events(client=client, searchDict={'farmerId': 10002})
    time2 = time.time()
    print '%s function took %0.5f ms' % ('read mongo for a dict', (time2 - time1) * 1000.0)

    print len(lst), lst[:3]
    # print lst
    time1 = time.time()
    lst = search_system_events(client=client, searchDict={'farmerId': 10001})
    time2 = time.time()
    print '%s function took %0.5f ms' % ('read mongo for a dict', (time2 - time1) * 1000.0)

    print len(lst), lst[:3]

    time1 = time.time()
    lst = search_system_events(client=client, searchDict={'farmerId': 10005})
    time2 = time.time()
    print '%s function took %0.5f ms' % ('read mongo for a dict', (time2 - time1) * 1000.0)

    print len(lst), lst

    time1 = time.time()
    lst = search_system_events(client=client, entityType='order')
    time2 = time.time()
    print '%s function took %0.5f ms' % ('read mongo for a dict', (time2 - time1) * 1000.0)

    print len(lst), lst[:5]

    time1 = time.time()
    lst = search_system_events(searchDict={'farmerId': 10002}, projection=[
        'eventType', 'eventName', 'entityType', 'entityId', 'timestamp', 'orderId', 'farmerId'
    ])
    time2 = time.time()
    print '%s function took %0.5f ms' % ('read mongo for a dict', (time2 - time1) * 1000.0)

    print len(lst), lst[:5]


def write_func():
    global client
    client = pymongo.MongoClient(client_url, maxPoolSize=100)
    db = create_temp_database()
    #db = get_test_db()
    random.seed(101)
    ev_list = generate_multiple_events(num=100000)

    time1 = time.time()
    insert_multiple_sms(db, ev_list)
    time2 = time.time()
    print '%s function took %0.5f ms' % ('write entries mongo with validation', (time2 - time1) * 1000.0)


if __name__ == '__main__':
    global client
    client = pymongo.MongoClient(client_url, maxPoolSize=100)
    write_func()
    #read_func()
