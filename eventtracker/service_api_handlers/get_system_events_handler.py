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

def get_system_events_list(params):


    validate_get_system_events(params)

    params.update({'searchDict':generate_searchDict(params)})
    events_list = search_system_events(**params)
    return events_list

def get_events(params):

    events_list = get_system_events_list(params)

    return events_list

if __name__== "__main__":
    pass