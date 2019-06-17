# pyshd #

[![pypi](https://img.shields.io/pypi/v/pyshd.svg)](https://pypi.python.org/pypi/pyshd)
[![travis](https://img.shields.io/travis/equinor/pyshd.svg?label=travis)](https://travis-ci.org/equinor/pyshd)
[![readthedocs](https://readthedocs.org/projects/pyshd/badge/?version=latest)](https://pyshd.readthedocs.io/en/latest/?badge=latest)

pyshd: pushd contextmanager for python

## Index ##

* [Introduction](#introduction)
* [Features](#features)
* [Getting started](#getting-started)
    * [Get from pypi](#get-from-pypi)
    * [Examples](#example)
* [Contributing](#contributing)

## Features ##

* Change directory in python using contextmanagers
* Free software: GNU Lesser General Public License v3

## Getting started ##

### Get from pypi ###

```pip install pyshd```

### Example ###

```python3
>>> from pyshd import pushd
>>> import os
>>> os.getcwd()
'/private/user/projects/pyshd'
>>> with pushd('/tmp'):
...     print(os.getcwd())
'/tmp'
>>> os.getcwd()
'/private/user/projects/pyshd'
```

## Contributing ##

We welcome all kinds of contributions, including code, bug reports, issues,
feature requests, and documentation.
