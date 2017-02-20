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


def get_system_events_list(params):
    kwargs = {}

    validate_get_system_events(params)
    events_list = search_system_events(kwargs)
    return events_list

def get_events(params):

    events_list = get_system_events_list(params)

    return events_list

if __name__== "__main__":
    pass