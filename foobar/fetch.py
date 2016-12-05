# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import requests


def fetch(url):
    return requests.get(url)


def fetch_with_dependency_injection(lib, url):
    if hasattr(lib, 'get'):
        return lib.get(url)

    return requests.get(url)
