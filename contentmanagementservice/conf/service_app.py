from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import django

# Init django. http://django.readthedocs.io/en/latest/releases/1.7.html#standalone-scripts
django.setup()

from agroutils.session.interfaces import DBInterface
from contentmanagementservice.utils.config import get_config_object
from contentmanagementservice.service_apis.content_upload import UploadContent
from contentmanagementservice.service_apis.featurelist import FeatureList
from contentmanagementservice.service_apis.help import help_api
from contentmanagementservice.service_apis.article import (
    Article, ArticleDetails, ActionOnArticle, LikedArticles
)
from contentmanagementservice.service_apis.template import Template

app = Flask('CMS')

app.config.from_object(get_config_object())

# Enable CORS. https://flask-cors.readthedocs.io/en/latest/#resource-specific-cors
CORS(app, resources={r"/contentmanagementservice/v1/*": {"origins": "*"}})

# Session
app.auth_header_name = 'X-Authorization-Token'
app.session_interface = DBInterface()

app.register_blueprint(help_api)

cms_api_v1 = Api(app, prefix='/contentmanagementservice/v1')
cms_api_v1.add_resource(UploadContent, '/upload/<string:content_type>/<string:script_name>')
cms_api_v1.add_resource(FeatureList, '/features/<string:script_type>/<string:content_type>')

content_api_v1 = Api(app, prefix='/contentservice/v1')
content_api_v1.add_resource(Article, '/article')
content_api_v1.add_resource(ArticleDetails, '/article/<string:article_id>/details')
content_api_v1.add_resource(ActionOnArticle, '/article/<string:article_id>/action')
content_api_v1.add_resource(LikedArticles, '/article/liked')
content_api_v1.add_resource(Template, '/template/<string:template_id>/', '/template/')

if __name__ == '__main__':
    app.logger.info("app {} started..".format(app))
    app.run(host="0.0.0.0", debug=True, port=8480)
