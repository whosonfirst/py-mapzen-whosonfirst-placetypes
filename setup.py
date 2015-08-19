#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.placetypes',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.placetypes'],
    version='0.03',
    description='Simple Python wrapper for managing Who\'s On First placetypes',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes',
    install_requires=[
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes/releases/tag/v0.03',
    license='BSD')
