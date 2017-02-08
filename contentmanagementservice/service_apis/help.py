from flask import Blueprint, jsonify
from flask import current_app as app

help_api = Blueprint('help_blueprint', __name__)


@help_api.route('/contentmanagementservice/')
@help_api.route('/contentmanagementservice/help')
def help():
    """Help"""
    func_list = {}
    # TODO: Doesn't handle url params
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)