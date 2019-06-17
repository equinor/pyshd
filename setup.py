#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name = 'pyshd',
    description = 'pyshd: pushd contextmanager for python',

    author = 'Equinor',
    author_email = 'jegm@equinor.com',
    url = 'https://github.com/equinor/pyshd',

    project_urls = {
        'Documentation': 'https://pyshd.readthedocs.io/',
        'Issue Tracker': 'https://github.com/equinor/pyshd/issues',
    },
    keywords = [
    ],

    license = 'GNU Lesser General Public License v3',

    packages = [
        'pyshd',
    ],
    platforms = 'any',

    install_requires = [
    ],

    setup_requires = [
        'setuptools >=28',
        'setuptools_scm',
        'pytest-runner'
    ],

    tests_require = [
        'pytest',
    ],



    use_scm_version = {
        'write_to': 'pyshd/version.py',
    },
)
