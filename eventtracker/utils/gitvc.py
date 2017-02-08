from git import Repo, Actor

from eventtracker.utils.logger import get_main_logger

logger = get_main_logger()


def git_commit(user, message, working_copy):
    # GitPython/gitpython Doc. http://gitpython.readthedocs.io/en/stable/index.html
    repo = Repo(working_copy)
    index = repo.index
    committer = Actor(user['name'], user['username'])
    repo.git.add('--all')  # git add --all
    commit_obj = index.commit(message, committer=committer)  # git commit -m "message"
    logger.info("Git commit. {}".format(commit_obj))
    return commit_obj