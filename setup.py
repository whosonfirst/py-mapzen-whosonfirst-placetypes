#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.placetypes.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst.placetypes',
    # namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.placetypes'],
    namespace_packages=['mapzen', 'mapzen.whosonfirst'],
    version=version,
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
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes/releases/tag/' + version,
    license='BSD')
