from os.path import expanduser


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseConfig(object):

    __metaclass__ = Singleton

    CONTENT_WORKING_COPY = "{}/cms-content".format(expanduser("~"))
    USER_SERVICE_URL = 'http://crm.agrostar.in/'
    ALLOWED_USER = ['nirmal', 'asha']
    DEFAULT_PAGE_LIMIT = 3
    IMAGES_API_REFERENCE = 'http://catalog.agrostar.in/static/'
    MONGO_URI = "mongodb://localhost:27017/content"

    LOGGER_CONFIG = {
        "loggers": {
            "main": {
                "level": "DEBUG",
                "propagate": False,
                "handlers": ["main"]
            },
            "crash": {
                "level": "ERROR",
                "propagate": False,
                "handlers": ["main", "server_err"]
            },
            "": {
                "level": "DEBUG",
                "handlers": ["default"]
            }
        },
        "handlers": {
            "main": {
                "level": "DEBUG",
                "formatter": "verbose",
                "class": "logging.StreamHandler"
            },
            "server_err": {
                "toaddrs": [
                    "hussaint@agrostar.in"
                ],
                "fromaddr": "cms@agrostar.in",
                "mailhost": [
                    "localhost",
                    25
                ],
                "formatter": "err_report",
                "class": "logging.handlers.SMTPHandler",
                "subject": "CMS Server Error"
            },
            "default": {
                "level": "DEBUG",
                "formatter": "verbose",
                "class": "logging.StreamHandler"
            }
        },
        "formatters": {
            "verbose": {
                "format": u"%(asctime)s [%(levelname)-8.8s] %(name)-8.8s [%(filename)-15.15s:%(lineno)-3.3s]: %(message)s"
            },
            "compact": {
                "format": u"%(asctime)s [%(levelname)-8.8s] %(name)-10.10s : %(message)s"
            },
            "err_report": {
                "format": u"%(asctime)s\n%(message)s"
            }
        },
        "version": 1
    }
