import importlib

from contentmanagementservice.utils.config import get_config_object
from contentmanagementservice.utils.filestore import save_file
from contentmanagementservice.utils.gitvc import git_commit
from contentmanagementservice.utils.logger import get_main_logger

logger = get_main_logger()
config_object = get_config_object()


def upload_handler(content_type, script_name, file, user, comment):
    """A generic upload handler for uploading any content."""
    logger.info("upload_handler :: {}".format(locals().copy()))
    working_copy = config_object.CONTENT_WORKING_COPY
    directory = "{}/{}/{}".format(working_copy, content_type, script_name)
    filename = save_file(file, directory)
    commit_obj = git_commit(user, comment, working_copy)
    # We must run the script in background
    # Good time to use python-rq. Maybe later.
    script_module = importlib.import_module('contentmanagementservice.scripts.upload.{}.{}'.format(content_type, script_name))
    # NOTE: A Dynamic factory implementation.
    # Every content_type module has a main method. Just import that module and call main.
    logger.info("script_module={}".format(script_module))
    return {
        'git_commit': commit_obj.name_rev,
        'script_response': script_module.main(filename)
    }


