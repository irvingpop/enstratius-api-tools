#!/usr/bin/env python

import enstratius_api_tools
import os
import glob

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ['mixcoatl==0.2.6', 'prettytable==0.6.1', 'argparse>=1.2.1']

packages=['enstratius_api_tools']

setup(
    name='enstratius_api_tools',
    version=enstratius_api_tools.__version__,
    description='enStratus API Client Interface',
    long_description=open('README.rst').read(),
    author='Greg Moselle',
    author_email='greg.moselle@enstratius.com',
    url='https://pypi.python.org/pypi/enstratius_api_tools',
    packages=packages,
    package_data={'': ['LICENSE', 'README.rst', 'requirements.txt']},
    package_dir={'enstratius_api_tools': 'enstratius_api_tools'},
    include_package_data=True,
    install_requires=requires,
		scripts=glob.glob(os.path.join('bin', '*')),
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ),
)
