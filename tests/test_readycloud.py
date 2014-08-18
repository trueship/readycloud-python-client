#!/usr/bin/env python
# coding: utf-8

"""
test_readycloud
----------------------------------

Tests for `readycloud.readycloud` module.
"""

import json
import unittest

from mock import patch, Mock

from readycloud import ReadyCloud
from readycloud.exceptions import ReadyCloudServerError


class ReadyCloudTestCase(unittest.TestCase):
    def setUp(self):
        self.rc = ReadyCloud(token='12345', host='https://readycloud.com/')

    def test_get_orders_url_should_return_full_orders_url(self):
        self.assertEqual(self.rc.get_orders_url(),
                         'https://readycloud.com/api/v1/orders/')

    def test_get_order_url_should_return_full_order_url_with_id(self):
        self.assertEqual(self.rc.get_order_url(1),
                         'https://readycloud.com/api/v1/orders/1/')

    def test_get_headers_should_return_right_headers(self):
        expected_headers = {
            'content-type': 'application/json',
            'AUTHORIZATION': 'bearer 12345',
        }
        self.assertEqual(self.rc.get_headers(), expected_headers)

    @patch('requests.get')
    def test_get_orders_should_send_get_with_right_params(self, get):
        self.rc.get_orders(limit=2)
        get.assert_called_once_with(
            'https://readycloud.com/api/v1/orders/',
            headers={
                'content-type': 'application/json',
                'AUTHORIZATION': 'bearer 12345'},
            params={'limit': 2})

    @patch('requests.post')
    def test_create_order_should_send_post_with_right_params(self, post):
        order = {
            'message': 'test',
        }
        self.rc.create_order(order)
        post.assert_called_once_with(
            'https://readycloud.com/api/v1/orders/',
            headers={
                'content-type': 'application/json',
                'AUTHORIZATION': 'bearer 12345'},
            data=json.dumps(order))

    @patch('requests.put')
    def test_update_order_should_send_put_with_right_params(self, put):
        order = {
            'message': 'test',
        }
        self.rc.update_order(1, order)
        put.assert_called_once_with(
            'https://readycloud.com/api/v1/orders/1/',
            headers={
                'content-type': 'application/json',
                'AUTHORIZATION': 'bearer 12345'},
            data=json.dumps(order))

    @patch('requests.delete')
    def test_delete_order_should_send_delete(self, delete):
        self.rc.delete_order(1)
        delete.assert_called_once_with(
            'https://readycloud.com/api/v1/orders/1/',
            headers={
                'content-type': 'application/json',
                'AUTHORIZATION': 'bearer 12345'})

    @patch('requests.get')
    def test_if_rc_returns_500_should_raise_exception(self, get):
        get.return_value = Mock(status_code=500)
        self.assertRaises(ReadyCloudServerError, self.rc.get_orders, limit=2)

    @patch('requests.post')
    def test_create_orders_webhooks_should_send_post_with_right_params(self,
                                                                       post):
        self.rc.create_orders_webhook('https://example.com/test')
        post.assert_called_once_with(
            'https://readycloud.com/api/v1/webhooks/',
            headers={
                'content-type': 'application/json',
                'AUTHORIZATION': 'bearer 12345'},
            data=json.dumps({
                'entity': 'orders',
                'url': 'https://example.com/test',
            }))

    @patch('requests.get')
    def test_get_webhooks_should_send_get_with_right_params(self, get):
        self.rc.get_webhooks(limit=2)
        get.assert_called_once_with(
            'https://readycloud.com/api/v1/webhooks/',
            headers={
                'content-type': 'application/json',
                'AUTHORIZATION': 'bearer 12345'},
            params={'limit': 2})

    @patch('requests.put')
    def test_update_orders_webhook_should_send_put_with_right_params(self,
                                                                     put):
        self.rc.update_orders_webhook(1, 'https://example.com/new-url')
        put.assert_called_once_with(
            'https://readycloud.com/api/v1/webhooks/1/',
            headers={
                'content-type': 'application/json',
                'AUTHORIZATION': 'bearer 12345'},
            data=json.dumps({
                'entity': 'orders',
                'url': 'https://example.com/new-url',
            }))

    @patch('requests.delete')
    def test_delete_webhook_should_send_delete(self, delete):
        self.rc.delete_webhook(1)
        delete.assert_called_once_with(
            'https://readycloud.com/api/v1/webhooks/1/',
            headers={
                'content-type': 'application/json',
                'AUTHORIZATION': 'bearer 12345'})

if __name__ == '__main__':
    unittest.main()
