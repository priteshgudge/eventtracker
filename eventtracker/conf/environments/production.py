from eventtracker.conf.environments.base import BaseConfig


class Config(BaseConfig):
    BaseConfig.LOGGER_CONFIG["handlers"]["main"]["level"] = "INFO"  # Log starting from INFO by default
    USER_SERVICE_URL = 'http://crm.agrostar.in/'
    MONGO_DB_URI = "mongodb://localhost:17017/"