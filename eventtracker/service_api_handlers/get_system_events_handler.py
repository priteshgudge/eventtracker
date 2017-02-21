import ast
import json
import logging
import pymongo
from bson import ObjectId
from agroutils.exceptions.agro_error import AgroError
from flask import current_app as app
from eventtracker.core.search_system_events import search_system_events
from eventtracker.utils.validation import validate_get_system_events

logger = logging.getLogger('main')

def generate_searchDict(params):
    search_dict = {}
    if 'farmerId' in params:
        search_dict['farmerId'] = params['farmerId']

    if 'orderId' in params:
        search_dict['orderId'] = params['orderId']

    if 'ticketId' in params:
        search_dict['ticketId'] = params['ticketId']
    return search_dict


full_projection = ['entityType', 'entityId', 'timestamp',
                   'eventType', 'eventName', 'farmerId',
                   'ticketId', 'orderId']


def get_system_events_list(params, details, offset, limit):

    #validate_get_system_events(params)

    params['offset'] = offset
    params['limit'] = limit
    if not details:
        params['projection'] = full_projection

    params.update({'searchDict':generate_searchDict(params)})

    events_list = search_system_events(**params)

    return events_list

def get_events(params):

    try:
        details = True if params.get('details','false') == 'true' else False
        offset = int(params.get('offset', 0))
        limit = int(params.get('limit', 10))
    except:
        raise AgroError(400, "Invalid Request")

    events_list = get_system_events_list(params, details, offset, limit)

    return events_list

if __name__== "__main__":
    pass