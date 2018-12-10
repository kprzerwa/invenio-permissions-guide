# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# test-access is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio digital library framework."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

INVENIO_VERSION = "3.1.0.dev20181106"

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('test_access', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='test-access',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='test-access Invenio',
    license='MIT',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/test-access/test-access',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'test-access = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'flask_debugtoolbar = flask_debugtoolbar:DebugToolbarExtension',
            'test_access_records = test_access.records:testaccess',
        ],
        'invenio_base.blueprints': [
            'test_access = test_access.theme.views:blueprint',
            'test_access_records = test_access.records.views:blueprint',
        ],
        'invenio_config.module': [
            'test_access = test_access.config',
        ],
        'invenio_i18n.translations': [
            'messages = test_access',
        ],
        'invenio_base.api_apps': [
            'test_access = test_access.records:testaccess',
         ],
        'invenio_jsonschemas.schemas': [
            'test_access = test_access.records.jsonschemas'
        ],
        'invenio_search.mappings': [
            'records = test_access.records.mappings'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
