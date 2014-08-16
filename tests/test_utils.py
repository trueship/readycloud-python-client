#!/usr/bin/env python
# coding: utf-8

"""
test_utils
----------------------------------

Tests for `readycloud.utils` module.
"""

import unittest

from mock import Mock

from readycloud.utils import urljoin, get_response_json


class UtilsTestCase(unittest.TestCase):
    def test_urljoin(self):
        self.assertEqual(urljoin('https://readycloud.com/', '/api/v1/orders/'),
                         'https://readycloud.com/api/v1/orders/')
        self.assertEqual(urljoin('https://readycloud.com', '/api/v1/orders/'),
                         'https://readycloud.com/api/v1/orders/')
        self.assertEqual(urljoin('https://readycloud.com', 'api/v1/orders'),
                         'https://readycloud.com/api/v1/orders/')

    def test_get_response_json_should_returns_json_with_status_code(self):
        response = Mock(
            json=lambda: {'test': 'test'},
            status_code=200,
            ok=True
        )
        self.assertEqual(
            get_response_json(response),
            {
                'test': 'test',
                'status_code': 200,
                'ok': True
            }
        )

    def test_get_repsonse_should_handle_non_json_response(self):
        def raise_exc():
            raise ValueError()

        response = Mock(
            json=raise_exc,
            status_code=200,
            ok=True,
            content='<h1>Test<h1>'
        )
        self.assertEqual(
            get_response_json(response),
            {
                'content': '<h1>Test<h1>',
                'status_code': 200,
                'ok': True
            }
        )

if __name__ == '__main__':
    unittest.main()
