import datetime

from agroutils.exceptions.agro_error import AgroError

LANGUAGES = ['en', 'gu', 'mr', 'hi']


reference_ts = datetime.datetime(2016,01,01,0,0,0,0)
class DocumentError(Exception):
    pass


entity_type_set = set(['order','ticket','farmer','product'])
event_type_set = set(['sms','email'])
event_name_set = set(['order_create_sms','order_edit_sms','order_cancel_sms',
                        'order_create_email','order_edit_email','order_cancel_email'
                       'ticket_create_sms','ticket_close_sms','ticket_status_change_sms'])


def validate_timestamp(timestamp):
    if not isinstance(timestamp, int):
        raise AgroError(400, "Invalid Timestamp")

    if not isinstance(timestamp,list):
        timestamp_list = [timestamp]
    else:
        timestamp_list = timestamp

    for t in timestamp_list:
        try:
            datet = datetime.datetime.fromtimestamp(float(t) / 1000.)
            now = datetime.datetime.now()
            if datet > now or datet < reference_ts:
                raise AgroError(400, "Invalid Timestamp")
        except:
            raise AgroError(400, "Invalid Timestamp")


def validate_entity_type(entity_type):
    if entity_type not in entity_type_set:
        raise AgroError(400, "Entity type is invalid")

    return True

def validate_event_type(event_type):
    if event_type not in event_type_set:
        raise AgroError(400, "Event type is invalid")

    return True

def validate_event_name(event_name):
    if event_name not in event_name_set:
        raise AgroError(400,"Event Name is invalid")

    return True


def validate_system_event(event_json):
    entity_type = event_json['entityType']
    entity_id = event_json['entityId']
    event_type = event_json['eventType']
    event_name = event_json['eventName']
    timestamp = event_json['timestamp']

    event_details = event_json['eventDetails']

    validate_entity_type(entity_type)
    validate_event_type(event_type)
    validate_event_name(event_name)
    validate_timestamp(timestamp)
    validate_additional_keys(event_json)

def validate_system_event_list(event_list):
    if not isinstance(event_list,list):
        raise AgroError(400, "Events is not a list")

    for event in event_list:
        validate_system_event(event)

    return True

def validate_system_event_request(request_details):

    if 'event' in request_details.keys():
        validate_system_event(request_details['event'])
    elif 'events' in request_details.keys():
        validate_system_event_list(request_details['events'])
    else:
        raise AgroError(400, "Bad Request. Need event/events in request")

def validate_additional_keys(request_details):
    if 'farmerId' in request_details.keys():
        if not isinstance(request_details['farmerId'], basestring):
            raise AgroError(400, "Invalid Farmer Id")

    if 'orderId' in request_details.keys():
        if not isinstance(request_details['orderId'], basestring):
            raise AgroError(400, "Invalid Order Id")

    if 'ticketId' in request_details.keys():
        if not isinstance(request_details['ticketId'], basestring):
            raise AgroError(400, "Invalid Ticket Id")

def check_search_keys(request_details):
    valid = False
    if 'farmerId' in request_details.keys():
        if not isinstance(request_details['farmerId'], basestring):
            return False
        valid = True
    if 'orderId' in request_details.keys():
        if not isinstance(request_details['orderId'], basestring):
            return False
        valid =  True

    if 'ticketId' in request_details.keys():
        if not isinstance(request_details['ticketId'], basestring):
            return False
        valid =  True

    return valid

def validate_get_system_events(request_details):

    valid = False

    if 'eventType' in request_details:
        event_type = request_details['eventType']
        if isinstance(event_type, list):
            for e in event_type:
                validate_event_type(e)
        else:
            validate_event_type(event_type)
        valid = True


    if 'entityType' in request_details:
        validate_entity_type(request_details['entityType'])
        if 'entityId' not in request_details:
            raise AgroError(400, "Enitity Ids are required")
        valid = True

    if 'timestamp' in request_details:
        validate_timestamp(request_details['timestamp'])

    if not valid and not check_search_keys(request_details):
        raise AgroError(400, "Invalid Request")

    return True