import importlib


def get_options(script_type, option_type):
    pkg = importlib.import_module('eventtracker.scripts.{}.{}'.format(script_type, option_type))
    return pkg.OPTIONS