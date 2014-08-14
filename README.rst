===============================
ReadyCloud API Client
===============================

.. image:: https://badge.fury.io/py/readycloud-python-client.png
    :target: http://badge.fury.io/py/readycloud-python-client

.. image:: https://travis-ci.org/trueship/readycloud-python-client.png?branch=master
        :target: https://travis-ci.org/trueship/readycloud-python-client

.. image:: https://pypip.in/d/readycloud-python-client/badge.png
        :target: https://pypi.python.org/pypi/readycloud-python-client


Python client for ReadyCloud API.

* Free software: BSD license
* Documentation: https://readycloud-python-client.readthedocs.org.

Features
--------

* GET, POST, PUT, DELETE requests to ReadyCloud.
* Order specific requests
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
