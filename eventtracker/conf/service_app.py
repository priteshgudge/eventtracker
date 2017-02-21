from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import django

# Init django. http://django.readthedocs.io/en/latest/releases/1.7.html#standalone-scripts
django.setup()

from agroutils.session.interfaces import DBInterface
from eventtracker.utils.config import get_config_object
from eventtracker.service_apis.help import help_api
from pymongo import MongoClient
from eventtracker.service_apis.system_event import SystemEvent

app = Flask('Event Tracker')

app.config.from_object(get_config_object())

# Enable CORS. https://flask-cors.readthedocs.io/en/latest/#resource-specific-cors
CORS(app, resources={r"/eventtracker/v1/*": {"origins": "*"}})

# Session
app.auth_header_name = 'X-Authorization-Token'
app.session_interface = DBInterface()
app.db_client = MongoClient(app.config['MONGO_DB_URI'],minPoolSize=5, maxPoolSize=100)

app.register_blueprint(help_api)

event_api_v1 = Api(app, prefix='/eventtracker/v1')
event_api_v1.add_resource(SystemEvent, '/systemevents/')

if __name__ == '__main__':
    app.logger.info("app {} started..".format(app))
    app.run(host="0.0.0.0", debug=True, port=7480)
