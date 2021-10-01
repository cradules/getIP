"""gunicorn WSGI server configuration."""

from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()


bind = '0.0.0.0:' + environ.get('PORT', '5000')
workers = max_workers()
keepalive = 1
timeout = 30
