# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages
from cargo import __version__

setup(
    name='cargo',
    version=__version__,
    author='Michel Meyer',
    author_email='michel@zazabe.fr',
    url='http://zazabe.fr',
    description='Social Graph - demo for Cargo Media',
    packages=find_packages(),
    include_package_data=True,
    dependency_links=[],
    install_requires=[
        'click>=4.0',
        'pytest>=2.7.1'
    ],
    entry_points='''
        [console_scripts]
        cargo=cargo.run:cli
    ''',
)
