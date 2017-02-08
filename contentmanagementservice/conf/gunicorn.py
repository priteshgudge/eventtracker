import os


def num_CPUs():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")


bind = "0.0.0.0:8480"
workers = num_CPUs() * 2 + 1
backlog = 2048
worker_class = "gevent"
debug = True
daemon = False
pidfile = "/tmp/cms-gunicorn.pid"
logfile = "/tmp/cms-gunicorn.log"
loglevel = 'info'
accesslog = '/tmp/gunicorn-access.log'
timeout = 50
