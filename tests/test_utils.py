#!/usr/bin/env python
# coding: utf-8

"""
test_utils
----------------------------------

Tests for `readycloud.utils` module.
"""

import unittest

from readycloud.utils import urljoin


class UtilsTestCase(unittest.TestCase):
    def test_urljoin(self):
        self.assertEqual(urljoin('https://readycloud.com/', '/api/v1/orders/'),
                         'https://readycloud.com/api/v1/orders/')
        self.assertEqual(urljoin('https://readycloud.com', '/api/v1/orders/'),
                         'https://readycloud.com/api/v1/orders/')
        self.assertEqual(urljoin('https://readycloud.com', 'api/v1/orders'),
                         'https://readycloud.com/api/v1/orders/')

if __name__ == '__main__':
    unittest.main()
