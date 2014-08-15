# coding: utf-8
"""
readycloud.decorators
----------------------------------

Module with decorators
"""

from functools import wraps

from .exceptions import ReadyCloudServerError


def safe_json_request(func):
    """
    Decorator which check response returned by func, and:

        - If status 20x or 40x - returns json deserialized response
        - If status 50x - raises ReadyCloudServerError
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        resp = func(*args, **kwargs)
        if resp.status_code == 500:
            raise ReadyCloudServerError(resp.content)
        return resp.json()
    return wrapper
