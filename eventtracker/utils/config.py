import os
import importlib


def get_config_object():
    agro_env = os.environ.get('AGRO_ENV', 'development') or 'development'
    module_name = 'eventtracker.conf.environments.{}'.format(agro_env)
    config_module = importlib.import_module(module_name)
    class_ = getattr(config_module, 'Config')
    return class_()
