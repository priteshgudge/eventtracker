# -*- coding: utf-8 -*-

import logging
from flask import current_app as app
from flask import request

from agroutils.restful.resource import patch_response_data, ok_response, error_response, Resource as AgroutilResource
from agroutils.session.auth import AuthenticationError
from eventtracker.utils.client import current_user
from agroutils.exceptions.error_handler import ErrorHandler
from eventtracker.utils.logger import send_exception_mail
from eventtracker.service_api_handlers.get_template_handler import get_template
crash_logger = logging.getLogger('crash')



class Template(AgroutilResource):
    @ErrorHandler("GET Template",app=app , exception_mailer=send_exception_mail)
    def get(self, template_id=None):
        app.logger.info("GET {}".format(self.__class__.__name__))
        params = request.args.to_dict()

        template = get_template(params)

        return ok_response(template)

    get.authenticated = False
