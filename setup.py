#!/usr/bin/env python
from setuptools import setup, find_packages

DESCRIPTION = "A python module which returns details about a Danish car from its license plate number"

try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    LONG_DESCRIPTION = ""
    pass

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

INSTALL_REQUIRES = ['requests', 'pyquery']
try:
    import importlib
except ImportError:
    INSTALL_REQUIRES.append('importlib')

tests_require = [
    'requests>=1.2',
    'pyquery'
]

setup(
    name='dk-car-scraper',
    version='1.0.0',
    #packages=find_packages(exclude=['tests', 'example']),
    author='Joshua Karjala-Svenden',
    author_email='joshua@fluxuries.com',
    url='https://github.com/joshuakarjala/dk-car-scraper/',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    include_package_data=True,
)