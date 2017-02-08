# -*- coding: utf-8 -*-

from flask import current_app as app
from flask.globals import request
import logging

from contentmanagementservice.service_api_handlers.content_upload_handler import upload_handler
from contentmanagementservice.utils.client import current_user
from agroutils.session.auth import AuthenticationError
from agroutils.restful.resource import patch_response_data, ok_response, error_response, Resource as AgroutilResource

crash_logger = logging.getLogger('crash')


class UploadContent(AgroutilResource):
    """Upload content"""

    method_decorators = [patch_response_data]  # NOTE: Overriden to remove @authenticate

    def post(self, content_type, script_name):
        app.logger.info("POST {} ({})".format(self.__class__.__name__, content_type))
        try:
            file = request.files['file']
            comment = request.args['comment']

            user = current_user(**request.headers)
            ########################  HACK  ##########################
            ## Only few users are allowed to use this api as of now ##
            assert user['guid'] in app.config['ALLOWED_USER'], "{} are only allowed to upload content".format(", ".join(app.config['ALLOWED_USER']))
            #########  Remove once permissions are handled  ##########
            params = dict(file=file, comment=comment, content_type=content_type, script_name=script_name,
                          user=dict(name=user['guid'], username=['guid']))

            response = upload_handler(**params)
            # NOTE: Transformation
            api_response = {
                'gitCommit': response['git_commit'],
                'scriptResponse': response['script_response']
            }
            return ok_response(api_response)
        except AuthenticationError as auth_err:
            crash_logger.exception(auth_err)
            return error_response(401, str(auth_err))
        except KeyError as key:
            crash_logger.exception(key)
            return error_response(400, "{} is required".format(key))
        except ValueError as val_err:
            crash_logger.exception(val_err)
            return error_response(400, str(val_err))
        except AssertionError as err:
            crash_logger.exception(err)
            return error_response(401, str(err))
        except Exception as err:
            crash_logger.exception(err)
            return error_response(500, str(err))
            # Note: str is important. err is tuple for some exceptions like IntegrityError

        # NOTE: Not used ErrorHandler. AuthenticationError is not there yet

    post.authenticated = True
