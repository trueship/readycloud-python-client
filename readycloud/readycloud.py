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
    """

    API_V1 = 'v1'
    API_V2 = 'v2'

    def __init__(self, token, host='https://readycloud.com/', org_id=None, api=API_V2):
        """
        :param str token: your bearer token
        :param str host: host with which you want to work (readycloud.com by default)
        :param str org_id: hexahexacontadecimal encoded organization id
        :param str api: api version (v2 by default)
        """
        self.token = token
        self.host = host
        self.api = api
        self.org_id = org_id

    @safe_json_request
    def get(self, url, params):
        """
        Do GET request to ReadyCloud.

        :param str url: URL to which you want to do request
        :param dict params: dict with request params
        :returns: dict -- dictionary with response
        """
        return requests.get(url, params=params, headers=self.get_headers())

    @safe_json_request
    def post(self, url, data):
        """
        Do POST request to ReadyCloud.

        :param str url: URL to which you want to do request
        :param dict data: dict with POST data
        :returns: dict -- dictionary with response
        """
        return requests.post(url, data=json.dumps(data), headers=self.get_headers())

    @safe_json_request
    def put(self, url, data):
        """
        Do PUT request to ReadyCloud.

        :param str url: URL to which you want to do request
        :param dict data: dict with data which you want to PUT
        :returns: dict -- dictionary with response
        """
        return requests.put(url, data=json.dumps(data), headers=self.get_headers())

    @safe_json_request
    def patch(self, url, data):
        """
        Do PATCH request to ReadyCloud.

        :param str url: URL to which you want to do request
        :param dict data: dict with data which you want to PUT
        :returns: dict -- dictionary with response
        """
        return requests.patch(url, data=json.dumps(data), headers=self.get_headers())

    @safe_json_request
    def delete(self, url):
        """
        Do DELETE request to ReadyCloud.

        :param str url: URL to which you want to do request
        :returns: dict -- dictionary with response
        """
        return requests.delete(url, headers=self.get_headers())

    def get_orders(self, **kwargs):
        """
        Get orders.

        :param dict kwargs: filters, limit, offset, etc.
        :returns: dict -- dictionary with response
        """
        return self.get(self.get_orders_url(), params=kwargs)

    def create_order(self, order):
        """
        Create a new order.

        :param dict order: dict structure of order
        :returns: dict -- dictionary with response
        """
        return self.post(self.get_orders_url(), data=order)

    def update_order(self, order_id, order):
        """
        Update an existing order.

        :param str order_id: order id
        :param dict order: dict structure of order
        :returns: dict -- dictionary with response
        """
        return self.put(self.get_order_url(order_id), data=order)

    def delete_order(self, order_id):
        """
        Delete order

        :param str order_id: order id for delete

        :returns: dict -- dictionary with response
        """
        return self.delete(self.get_order_url(order_id))

    def create_orders_webhook(self, url):
        """
        Create new webhook for orders.

        :param str url: URL to which RS should post updated for orders

        :returns: dict -- dictionary with response
        """
        return self.create_webhook('orders', url)

    def update_orders_webhook(self, webhook_id, url):
        """
        Update URL for already registered orders webhook.

        :param int webhook_id: webhook id which you want to edit
        :param str url: new webhook url

        :returns: dict -- dictionary with response
        """
        return self.update_webhook(webhook_id, 'orders', url)

    def get_webhooks(self, **kwargs):
        """
        Get list of registered webhooks
        :param dict kwargs: filters, limit, offset, etc.

        :returns: dict -- dictionary with response
        """
        return self.get(self.get_webhooks_url(), params=kwargs)

    def create_webhook(self, entity, url):
        """
        Create new webhook.

        :param str entity: Entity for which you want to register webhook
        :param str url: URL to which RC should post updates for registered entity

        :returns: dict -- dictionary with response
        """
        data = {
            'entity': entity,
            'url': url,
        }
        return self.post(self.get_webhooks_url(), data=data)

    def update_webhook(self, webhook_id, entity, url):
        """
        Update an existing webhook.

        :param int webhook_id: order id
        :param str entity: Entity for which you want to register webhook
        :param str url: URL to which RC should post updates for registered entity
        :returns: dict -- dictionary with response
        """
        data = {
            'entity': entity,
            'url': url,
        }
        return self.put(self.get_webhook_url(webhook_id), data=data)

    def delete_webhook(self, webhook_id):
        """
        Delete webhook

        :param int webhook_id: webhook id for delete

        :returns: dict -- dictionary with response
        """
        return self.delete(self.get_webhook_url(webhook_id))

    def get_organization(self, org_id):
        """
        Get organization.
        :param str org_id: hexahexacontadecimal encoded organization id
        :returns: dict -- dictionary with response
        """
        return self.get(self.get_organization_url(org_id), params={})

    def get_organizations(self, **kwargs):
        """
        Get organization.
        :param dict kwargs: filters, limit, offset, etc.
        :returns: dict -- dictionary with response
        """
        return self.get(self.get_organizations_url(), params=kwargs)

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
        Get orders endpoint URL.

        :returns: str -- absolute URL to orders endpoint
        """

        if self.api == self.API_V1:
            uri = '/api/v1/orders/'
        elif self.api == self.API_V2:
            if not self.org_id:
                raise ValueError('org_id should be set')
            uri = '/api/v2/orgs/{0}/orders/'.format(self.org_id)
        else:
            raise NotImplementedError()
        return urljoin(self.host, uri)

    def get_order_url(self, order_id):
        """
        Get orders endpoint URL for specified order_id

        :param str order_id: order id

        :returns: str -- absolute URL to order endpoint
        """
        return urljoin(self.get_orders_url(), str(order_id))

    def get_webhooks_url(self):
        """
        Get webhooks endpoint URL.

        :returns: str -- absolute URL to webhooks endpoint
        """
        return urljoin(self.host, '/api/v1/webhooks/')

    def get_webhook_url(self, webhook_id):
        """
        Get webhooks endpoint URL for specified webhook_id

        :param int webhook_id: webhook id

        :returns: str -- absolute URL to webhook endpoint
        """
        return urljoin(self.get_webhooks_url(), str(webhook_id))

    def get_organization_url(self, org_id):
        """
        Get organization endpoint URL
        :param str org_id: hexahexacontadecimal encoded organization id
        :returns: str -- absolute URL to organization endpoint
        """
        return urljoin(self.host, '/api/v2/orgs/{0}'.format(org_id))

    def get_organizations_url(self):
        """
        Get organizations endpoint URL
        :returns: str -- absolute URL to organizations endpoint
        """
        return urljoin(self.host, '/api/v2/orgs/')
