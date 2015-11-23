===============================
ReadyCloud API Client
===============================

.. image:: https://badge.fury.io/py/readycloud.png
    :target: http://badge.fury.io/py/readycloud

.. image:: https://travis-ci.org/trueship/readycloud-python-client.png?branch=master
        :target: https://travis-ci.org/trueship/readycloud-python-client

.. image:: https://pypip.in/d/readycloud/badge.png
        :target: https://pypi.python.org/pypi/readycloud


Python client for ReadyCloud API.

* Free software: BSD license
* Documentation: https://readycloud-python-client.readthedocs.org.

Features
--------

* GET, POST, PUT, PATCH, DELETE requests to ReadyCloud.
* CRUD functions for Order, WebHooks
* Support for Python2 and Python3.

Installation
------------

.. code-block:: bash

    pip install readycloud

Usage
-----

.. code-block:: python

    from readycloud import ReadyCloud
    rc = ReadyCloud(token='your token')

    orders = rc.get_orders()

    order = orders['objects']['0']
    order['message'] = 'New message'

    rc.update_order(order['id'], order)

    rc.delete_order(order['id'])

    boxes = rc.get('/api/v1/boxes')
