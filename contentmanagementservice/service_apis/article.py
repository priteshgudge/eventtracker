# -*- coding: utf-8 -*-

import logging
from flask import current_app as app
from flask import request

from agroutils.restful.resource import patch_response_data, ok_response, error_response, Resource as AgroutilResource
from agroutils.session.auth import AuthenticationError
from contentmanagementservice.utils.client import current_user
from contentmanagementservice.service_api_handlers.article_handler import (
    get_articles, get_one_article, user_likes_count, put_article_action,
    is_article_liked_by_user, article_likes_count, get_liked_articles
)
from contentmanagementservice.utils.validation import DocumentError

crash_logger = logging.getLogger('crash')


class Article(AgroutilResource):

    def get(self):
        try:
            app.logger.info("GET {}".format(self.__class__.__name__))
            params = request.args.to_dict()

            articles, total = get_articles(**params)

            if params.get('likes', 'true') == 'true':
                for article in articles:
                    article.update(likes=article_likes_count(article['_id']))
            response = dict(articles=articles, total=total)
            return ok_response(response)
        except AssertionError as err:
            crash_logger.exception(err)
            return error_response(400, str(err))
        except ValueError as val_err:
            crash_logger.exception(val_err)
            return error_response(400, 'Invalid param value')
        except TypeError as type_err:
            crash_logger.exception(type_err)
            return error_response(400, 'Invalid param')
        except Exception as gen_err:
            crash_logger.exception(gen_err)
            return error_response(500, 'Something went wrong')

    get.authenticated = False


class ArticleDetails(AgroutilResource):

    # NOTE: Override decorators to remove default @authenticate
    method_decorators = [patch_response_data]

    def get(self, article_id):
        try:
            app.logger.info("GET article/{}".format(article_id))

            params = request.args.to_dict()
            user = current_user(**request.headers)
            user_id = user['user_id']
            article = get_one_article(article_id, **params)
            response = dict(
                article=article,
                liked=is_article_liked_by_user(article_id, user_id),
                user_likes=user_likes_count(user_id),
                likes=article_likes_count(article_id)
            )
            return ok_response(response)
        except DocumentError as doc_err:
            crash_logger.exception(doc_err)
            return error_response(404, str(doc_err))
        except AuthenticationError as auth_err:
            crash_logger.exception(auth_err)
            return error_response(401, str(auth_err))
        except Exception as gen_err:
            crash_logger.exception(gen_err)
            return error_response(500, 'Something went wrong')

    get.authenticated = True


class ActionOnArticle(AgroutilResource):

    method_decorators = [patch_response_data]

    def put(self, article_id):
        try:
            app.logger.info("GET article/{}".format(article_id))
            user = current_user(**request.headers)
            user_id = user['user_id']
            params = request.get_json()
            params.update(article_id=article_id, user_id=user_id)
            response = put_article_action(**params)
            return ok_response(response)
        except DocumentError as doc_err:
            crash_logger.exception(doc_err)
            return error_response(404, str(doc_err))
        except AuthenticationError as auth_err:
            crash_logger.exception(auth_err)
            return error_response(401, str(auth_err))
        except Exception as gen_err:
            crash_logger.exception(gen_err)
            return error_response(500, 'Something went wrong')

        put.authenticated = True


class LikedArticles(AgroutilResource):

    method_decorators = [patch_response_data]

    def get(self):
        try:
            app.logger.info("GET /article/liked")
            params = request.args.to_dict()

            user = current_user(**request.headers)
            user_id = user['user_id']

            articles, total = get_liked_articles(user_id, **params)

            # NOTE: Assumed get liked articles is not paginated
            response = dict(articles=articles, user_likes=total)
            return ok_response(response)
        except AuthenticationError as auth_err:
            crash_logger.exception(auth_err)
            return error_response(401, str(auth_err))
        except Exception as gen_err:
            crash_logger.exception(gen_err)
            return error_response(500, 'Something went wrong')

    get.authenticated = True


