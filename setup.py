#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    "requests",
]

test_requirements = [
    "mock",
]

setup(
    name='readycloud',
    version='0.2.0',
    description='Python client for ReadyCloud API.',
    long_description=readme + '\n\n' + history,
    author='TrueShip, LLC',
    author_email='tlyapun@trueship.com',
    url='https://github.com/trueship/readycloud-python-client',
    packages=[
        'readycloud',
    ],
    package_dir={'readycloud': 'readycloud'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='readycloud-python-client',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
