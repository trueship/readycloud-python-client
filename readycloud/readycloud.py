# coding: utf-8
"""
readycloud.readycloud
----------------------------------

Module which contains ReadyCloud class.
"""

import requests
import json

from .decorators import safe_json_request
from .utils import urljoin


class ReadyCloud(object):
    """
    Class for working with ReadyCloud API.

    :param token: your bearer token
    :type token: str
    :param host: host with which you want to work (readycloud.com by default)
    :type host: str
    """
    def __init__(self, token, host='https://readycloud.com/'):
        self.token = token
        self.host = host

    @safe_json_request
    def get(self, url, params):
        """
        Do GET request to ReadyCloud.

        :param url: url to which you want to do request
        :type url: str
        :param params: dict with request params
        :type params: dict
        :returns: dict -- dictionary with response
        """
        return requests.get(url, params=params, headers=self.get_headers())

    @safe_json_request
    def post(self, url, data):
        """
        Do POST request to ReadyCloud.

        :param url: url to which you want to do request
        :type url: str
        :param data: dict with POST data
        :type data: dict
        :returns: dict -- dictionary with response
        """
        return requests.post(url, data=data, headers=self.get_headers())

    @safe_json_request
    def put(self, url, data):
        """
        Do PUT request to ReadyCloud.

        :param url: url to which you want to do request
        :type url: str
        :param data: dict with data which you want to PUT
        :type data: dict
        :returns: dict -- dictionary with response
        """
        return requests.put(url, data=data, headers=self.get_headers())

    @safe_json_request
    def delete(self, url):
        """
        Do DELETE request to ReadyCloud.

        :param url: url to which you want to do request
        :type url: str
        :returns: dict -- dictionary with response
        """
        return requests.delete(url, headers=self.get_headers())

    def get_orders(self, **kwargs):
        """
        Get orders.

        :param **kwargs: filters, limit, offset, etc.
        :type kwargs: str
        :returns: dict -- dictionary with response
        """
        return self.get(self.get_orders_url(), params=kwargs)

    def create_order(self, order):
        """
        Create a new order.

        :param order: dict structure of order
        :type order: dict
        :returns: dict -- dictionary with response
        """
        return self.post(self.get_orders_url(), data=json.dumps(order))

    def update_order(self, order_id, order):
        """
        Update an existing order.

        :param order_id: order id
        :type order_id: int
        :param order: dict structure of order
        :type order: dict
        :returns: dict -- dictionary with response
        """
        return self.put(self.get_order_url(order_id), data=json.dumps(order))

    def delete_order(self, order_id):
        """
        Delete order

        :param order_id: order id for delete
        :type order_id: int

        :returns: dict -- dictionary with response
        """
        return self.delete(self.get_order_url(order_id))

    def get_headers(self):
        """
        Get http headers for request.

        :returns: dict -- dictionary with headers
        """
        return {
            'content-type': 'application/json',
            'AUTHORIZATION': 'bearer {0}'.format(self.token),
        }

    def get_orders_url(self):
        """
        Get orders endpoint url.

        :returns: str -- absolute url to orders endpoint
        """
        return urljoin(self.host, '/api/v1/orders/')

    def get_order_url(self, order_id):
        """
        Get orders endpoint url for specified order_id

        :param order_id: order id
        :type order_id: int

        :returns: str -- absolute url to order endpoint
        """
        return urljoin(self.get_orders_url(), str(order_id))
