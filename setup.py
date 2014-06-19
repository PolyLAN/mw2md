# -*- coding: utf-8 -*-
try:
    from ez_setup import use_setuptools
    use_setuptools()
except:
    pass

from setuptools import setup, find_packages
import sys

_requires = ["creole", "html2text"]

setup(
      name = 'PyLDPath',
      version = '0.0.1',
      description = 'MediaWiki to MarkDown syntax translation',
      long_description = 'Simple library to translate between those common docuemntation syntaxes.',
      license = 'Apache License, Version 2.0', #Should be removed by PEP  314
      author = "Sergio Fernández",
      author_email = "sergio.fernandez@salzburgresearch.at",
      url = 'http://bitbucket.org/wikier/mw2md',
      platforms = ['any'], #Should be removed by PEP  314
      packages = ['mw2md'],
      requires = _requires, # Used by distutils to create metadata PKG-INFO
      install_requires = _install_requires, #Used by setuptools to install the dependencies
      classifiers =  [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
      ],
      keywords = 'python mediawiki markdown',
      use_2to3 = True,
      #requires_python = '>=2.5', # Future in PEP 345
      #scripts = ['ez_setup.py']
)

