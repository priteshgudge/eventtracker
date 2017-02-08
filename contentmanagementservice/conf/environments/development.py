from contentmanagementservice.conf.environments.base import BaseConfig


class Config(BaseConfig):
    USER_SERVICE_URL = 'http://localhost:7281/'
    MONGO_URI = "mongodb://localhost:27017/content"
    MONGO_DB_URI = "mongodb://localhost:27017/"
