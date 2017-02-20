import logging
from flask import current_app as app
from flask import request

from agroutils.restful.resource import patch_response_data, ok_response, error_response, Resource as AgroutilResource
from agroutils.session.auth import AuthenticationError
from eventtracker.utils.client import current_user
from agroutils.exceptions.error_handler import ErrorHandler
from agroutils.exceptions.agro_error import AgroError
from eventtracker.service_api_handlers.post_system_events_handler import post_system_event
from eventtracker.service_api_handlers.get_system_events_handler import get_events
from eventtracker.utils.logger import send_exception_mail
crash_logger = logging.getLogger('crash')



class SystemEvent(AgroutilResource):
    @ErrorHandler("GET System Events",app=app , exception_mailer=send_exception_mail)
    def get(self, event_id=None):
        app.logger.info("GET {}".format(self.__class__.__name__))
        params = request.args.to_dict()

        response = None

        return ok_response(response)

    get.authenticated = False

    @ErrorHandler("POST System Events",app=app , exception_mailer=send_exception_mail)
    def post(self):
        app.logger.info("POST {}".format(self.__class__.__name__))

        try:
            request_details = request.json
        except:
            raise AgroError(400, "Bad Request")

        response,code = post_system_event(request_details)


        return ok_response(response, code=code)

    post.authenticated = False
