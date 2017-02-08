import logging
import logging.config
from agroutils.mail import send

from contentmanagementservice.utils.config import get_config_object


def get_main_logger():
    logging.config.dictConfig(get_config_object().LOGGER_CONFIG)
    logger = logging.getLogger('main')
    return logger


def get_root_logger():
    logging.config.dictConfig(get_config_object().LOGGER_CONFIG)
    logger = logging.getLogger()
    return logger


def send_exception_mail(exception_str, api_key):
    try:
        subject_param = 'CRMService Error Notification for ' + api_key + " API "
        to_param = ['Assisted eCommerce <a-ecom@agrostar.in>']
	send_exception_mails = app.config.get('SEND_EXCEPTION_MAILS')
	if send_exception_mails:
            send(exception_str, subject=subject_param, to=to_param)
    except:
        pass
