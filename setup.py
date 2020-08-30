#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

from ast import literal_eval
import os
DOCKER_DEV = literal_eval(os.environ.get("DEV_CSCI_UTILS", "0"))

def read(*names, **kwargs):
    try:
        with io.open(
            join(dirname(__file__), *names),
            encoding=kwargs.get('encoding', 'utf8')
        ) as fh:
            return fh.read()
    except FileNotFoundError:
        if DOCKER_DEV:
            return ""
        raise

setup(
    name='csci-utils',
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        "local_scheme": "node-and-timestamp",
        #'local_scheme': 'dirty-tag',
        #'write_to': 'src/csci_utils/_version.py',
        #'fallback_version': '0.0.0',
    } if not DOCKER_DEV else False,
    description='An example package. Generated with cookiecutter-pylibrary.',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Feng Gao',
    author_email='feg264@g.harvard.edu',
    url='https://github.com/csci-e-29/2020sp-csci-utils-VinceGa',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
        'Private :: Do Not Upload',
    ],
    project_urls={
        'Changelog': 'https://github.com/csci-e-29/2020sp-csci-utils-VinceGa/blob/master/CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/csci-e-29/2020sp-csci-utils-VinceGa/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.6',
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
        'atomicwrites>=1.2.0',
        'luigi',
        'toolz',
        'fsspec>=0.3.3',
        'numpy',
        'pandas',
        'dask'



    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
        'setuptools_scm>=3.3.1',
        
    ],
    entry_points={
        'console_scripts': [
            'csci-utils = csci_utils.cli:main',
        ]
    },
)
