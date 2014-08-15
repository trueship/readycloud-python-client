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
