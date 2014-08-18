# coding: utf-8
"""
readycloud.utils
----------------------------------

Module which contains different utils, helpers, etc.
"""


def urljoin(*args):
    """
    Join provided url parts to url

    :param *args: url parts to join
    :type *args: str
    :returns: str -- concatenated url
    """
    return '/'.join(s.strip('/') for s in args) + '/'


def get_response_json(response):
    """
    Safe loads JSON response. If response is not json serialized - return it
    as content key.

    :param response: response
    :type response: requests response object
    :returns: dict -- dictionary with loaded json response
    """
    try:
        response_json = response.json()
    except ValueError:
        response_json = {
            'content': response.content,
        }
    response_json.update({
        'status_code': response.status_code,
        'ok': response.ok,
    })
    return response_json
