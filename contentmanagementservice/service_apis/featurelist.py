from flask import current_app as app
import logging

from contentmanagementservice.service_api_handlers.options_handler import get_options
from agroutils.restful.resource import ok_response, error_response, Resource as AgroutilResource

crash_logger = logging.getLogger('crash')


class FeatureList(AgroutilResource):
    """Options to be used for populating dropdowns"""

    def get(self, script_type, content_type):
        app.logger.info("GET {} {}/{}".format(self.__class__.__name__, script_type, content_type))
        try:
            response = get_options(script_type, content_type)
            return ok_response(response)
        except ImportError as imp_err:
            crash_logger.exception(imp_err)
            return error_response(400, 'Either script or option type invalid')
        except Exception as err:
            crash_logger.exception(err)
            return error_response(500, str(err))

    get.authenticated = False
