# -*- coding: utf-8 -*-
import re
import os.path

from setuptools import setup, find_packages

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing  # noqa
except ImportError:
    pass


def find_version(*path):
    version_file = open(os.path.join(os.path.dirname(__file__), *path)).read()
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                              version_file, re.M)

    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version.')


# Extra commands for documentation management
cmdclass = {}
command_options = {}

# Build Sphinx documentation (html)
# python setup.py build_sphinx
# generates files into build/sphinx/html
try:
    from sphinx.setup_command import BuildDoc
    cmdclass['build_sphinx'] = BuildDoc
except ImportError:
    pass


# Upload Sphinx documentation to PyPI (using Sphinx-PyPI-upload)
# python setup.py build_sphinx
# updates documentation at http://packages.python.org/tarantool/
try:
    from sphinx_pypi_upload import UploadDoc
    cmdclass['upload_sphinx'] = UploadDoc
    command_options['upload_sphinx'] = {
        'upload_dir': (
            'setup.py',
            os.path.join(os.path.dirname(__file__), 'build', 'sphinx', 'html')
        )
    }
except ImportError:
    pass


setup(
    name='tarantool',
    packages=find_packages(exclude=['tests', 'tests.tarantool']),
    version=find_version('tarantool', '__init__.py'),
    install_requires=[
        'six==1.2.0',
    ],
    tests_require=[
        'nose==1.2.1',
    ],
    test_suite='nose.collector',
    platforms=['all'],
    author='Konstantin Cherkasoff',
    author_email='k.cherkasoff@gmail.com',
    url='https://github.com/coxx/tarantool-python',
    license='BSD',
    description='Python client library for Tarantool Database',
    long_description=open('README.rst').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Front-Ends'
    ],
    cmdclass=cmdclass,
    command_options=command_options
)
