from contentmanagementservice.conf.environments.base import BaseConfig


class Config(BaseConfig):
    USER_SERVICE_URL = 'http://crmtest.agrostar.in/'
    MONGO_DB_URI = "mongodb://localhost:27017/"