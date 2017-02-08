import logging

from agroutils.userclient.user_service_client import UserServiceClient
from agroutils.session.auth import AuthenticationError
from eventtracker.utils.config import get_config_object

logger = logging.getLogger('main')


def current_user(**kwargs):
    logger.info("current_user :: {}".format(locals().copy()))
    config_object = get_config_object()
    UserServiceClient.url = config_object.USER_SERVICE_URL
    UserServiceClient.xauth_token = kwargs['X-Authorization-Token']
    logger.info("final url = {}".format(UserServiceClient.url))
    status, user = UserServiceClient.current_user(source=kwargs.get('source'))
    if not status:
        raise AuthenticationError('Authentication failure')
    return user['responseData']