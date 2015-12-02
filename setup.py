#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.placetypes',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.placetypes'],
    version='0.09',
    description='Simple Python wrapper for managing Who\'s On First placetypes',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes',
    install_requires=[
        # note that we are not requiring pygraphviz (used by the wof-graph-placetypes
        # script below) here since that seems like an excessive dependency which maybe
        # means the script should be in a separate which is a thing that could happen
        # ... but not today (20151202/thisisaaronland)
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-graph-placetypes'
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes/releases/tag/v0.09',
    license='BSD')
