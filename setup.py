#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mnowotka'

import sys

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

if sys.version_info < (2, 7, 3) or sys.version_info >= (3, 0, 0):
    raise Exception('ChEMBL software stack requires python 2.7.3 - 3.0.0')

setup(
    name='chembl_webservices',
    version='0.5.21',
    author='Michal Nowotka',
    author_email='mnowotka@ebi.ac.uk',
    description='Python package providing chembl webservices API.',
    url='https://www.ebi.ac.uk/chembldb/index.php/ws',
    license='CC BY-SA 3.0',
    packages=['chembl_webservices'],
    long_description=open('README.rst').read(),
    install_requires=[
        'lxml',
        'defusedxml>=0.4.1',
        'simplejson==2.3.2',
        'Pillow>=2.1.0',
        'django-tastypie==0.12',
        'chembl_core_model>=0.5.8',
        'cairocffi>=0.5.1',
        'numpy>=1.7.1',
        'mimeparse',
        'raven>=3.5.0',
    ],
    include_package_data=True,
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: Creative Commons :: Attribution-ShareAlike 3.0 Unported',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Scientific/Engineering :: Chemistry'],
    zip_safe=False,
)
