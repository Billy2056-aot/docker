#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
"""
requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.
"""
from certifi import where
from _pydecimal import __name__
import requests 
requests.get('https://github.com' , verify=True)

if __name__ == '__main__':
    print(where())
