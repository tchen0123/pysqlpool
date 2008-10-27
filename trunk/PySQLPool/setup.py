#!/usr/bin/env python

from distutils.core import setup
import PySQLPool

setup(name='PySQLPool',
      version=PySQLPool.__version__,
      description='Python MySQL Connection Pooling and MySQL Query management',
      author='Nick Verbeck',
      author_email='nick@skeletaldesign.com',
      url='http://code.google.com/p/pysqlpool/',
      download_url="http://code.google.com/p/pysqlpool/downloads/list",
      packages=['PySQLPool'],
     )