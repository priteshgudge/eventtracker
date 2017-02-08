import ast
import json
import logging
import pymongo
from bson import ObjectId
from bson.dbref import DBRef
from datetime import datetime

from contentmanagementservice.utils.encoder import BsonToJsonEncoder
from contentmanagementservice.utils.validation import LANGUAGES, DocumentError
from contentmanagementservice.utils.config import get_config_object

config = get_config_object()
client = pymongo.MongoClient()
db = client.content
logger = logging.getLogger('main')


def search_articles(**kwargs):
    """
    Search articles
    :param language: str
    :param limit: int
    :param offset: int
    :param exclude: list
    :param projection: dict
    :param trasform: bool
    :param type: str
    :param tags: list
    :param likes: bool
    :return: list of articles
    :rtype: list
    """

    logger.info("search_articles :: {}".format(locals().copy()))

    cursor = db.articles

    language = kwargs.get('language', 'en') or 'en'
    assert language in LANGUAGES, "Invalid language '{}'".format(language)

    projection = kwargs.get('projection', {}) or {}
    transform = kwargs.get('transform', True)

    query = dict()
    exclude = kwargs.get('exclude')
    if exclude and isinstance(exclude, list):
        query.update({'_id': {'$nin': map(ObjectId, exclude)}})

    include = kwargs.get('include')
    if isinstance(include, list):
        query.update({'_id': {'$in': map(ObjectId, include)}})

    type_param = kwargs.get('type')
    if type_param:
        query.update({'type.code': type_param})

    tags = kwargs.get('tags')
    if tags and isinstance(tags, list):
        query.update({'tags.code': {'$in': [tag for tag in tags]}})

    if projection:
        cursor = cursor.find(query, projection)
    else:
        cursor = cursor.find(query)

    total = cursor.count()

    offset = kwargs.get('offset')
    if offset:
        cursor = cursor.skip(abs(int(offset)))

    limit = kwargs.get('limit')
    if limit:
        cursor = cursor.limit(abs(int(limit)))

    articles_list = []
    for _article in cursor:
        if transform:
            _article = transform_article(_article, language)
        articles_list.append(_article)

    return articles_list, total


def transform_article(article, language):
    if article.get('type'):
        article['type'].update(article['type'].pop('descriptions')[language])

    if article.get('source'):
        article['source'].update(article['source'].pop('descriptions')[language])

    if article.get('tags'):
        tags = []
        for tag in article['tags']:
            tag.update(tag.pop('descriptions')[language])
            tags.append(tag)
        article.update(tags=tags)

    if article.get('descriptions'):
        article.update(article.pop('descriptions')[language])

    images = article.get('images')
    if images and isinstance(images, list):
        article.update(images=['{}{}'.format(config.IMAGES_API_REFERENCE, image) for image in images])

    article_dict = json.loads(json.dumps(article, cls=BsonToJsonEncoder))

    return article_dict


def get_articles(**kwargs):
    kwargs['limit'] = kwargs.get('limit', config.DEFAULT_PAGE_LIMIT) or config.DEFAULT_PAGE_LIMIT
    exclude = kwargs.get('exclude')
    if exclude:
        # Passing list from android was too much hassle so using comma separated items instead
        kwargs['exclude'] = [e.strip() for e in exclude.split(',')]
    tags = kwargs.get('tags')
    if tags:
        kwargs['tags'] = [t.strip() for t in tags.split(',')]
    kwargs['language'] = kwargs.get('language', 'en') or 'en'
    # ignore description for article list api
    kwargs.update(projection={'descriptions.{}.description'.format(kwargs['language']): 0})

    return search_articles(**kwargs)


def get_one_article(article_id, **kwargs):
    articles, _ = search_articles(include=[article_id], **kwargs)
    if not articles:
        raise DocumentError("article {} not found".format(article_id))
    return articles[0]


def user_likes_count(user_id):
    collection = db.article_user_actions
    query = {'user_id': user_id, 'action': 'like'}
    user_likes = collection.find(query).count()
    return user_likes


def article_likes_count(article_id):
    collection = db.article_user_actions
    query = {'article_id': article_id, 'action': 'like'}
    likes = collection.find(query).count()
    return likes


def is_article_liked_by_user(article_id, user_id):
    collection = db.article_user_actions
    article_user_action = collection.find_one({'article_id': article_id, 'user_id': user_id, 'action': 'like'})
    return True if article_user_action else False


def get_article_action_count(**kwargs):
    collection = db.article_user_actions
    return collection.find(kwargs).count()


def get_article_like_count(**kwargs):
    kwargs.update(action='like')
    return get_article_action_count(**kwargs)


def get_liked_articles(user_id, **kwargs):
    collection = db.article_user_actions
    query_liked_article_ids = collection.find({'user_id': user_id, 'action': 'like'}, {'article_id': 1})
    liked_article_ids = []
    for item in query_liked_article_ids:
        liked_article_ids.append(item['article_id'])

    liked_articles, total = search_articles(include=liked_article_ids, **kwargs)

    return liked_articles, total


def put_article_action(**kwargs):
    logger.info("put_article_action :: {}".format(locals().copy()))
    article = get_one_article(kwargs['article_id'], transform=False)
    kwargs.update(article_code=article['code'])
    put_article_user_action(**kwargs)
    add_log('article', kwargs)
    kwargs.pop('user_id')
    like_count = get_article_like_count(**kwargs)
    return dict(likes=like_count)


# TODO: Add json schema validation
def put_article_user_action(**kwargs):
    logger.info("put_article_user_action :: {}".format(locals().copy()))
    collection = db.article_user_actions
    response = collection.update({'user_id': kwargs['user_id'], 'article_code': kwargs['article_code']}, kwargs, upsert=True)
    return response


def add_log(type, data):
    collection = db.log
    log = dict(
        type=type,
        date=datetime.now(),
        data=data
    )
    return collection.insert_one(log).inserted_id
