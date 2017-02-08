import importlib


def get_options(script_type, option_type):
    pkg = importlib.import_module('contentmanagementservice.scripts.{}.{}'.format(script_type, option_type))
    return pkg.OPTIONS