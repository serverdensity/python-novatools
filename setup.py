import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = ['httplib2', 'argparse', 'prettytable']
if sys.version_info < (2,6):
    requirements.append('simplejson')

setup(
    name = "python-novatools",
    version = "2.0-serverdensity5",
    description = "Client library for OpenStack Nova API",
    long_description = read('README.rst'),
    url = 'https://github.com/rackspace/python-novatools',
    license = 'BSD',
    author = 'Rackspace, based on work by Jacob Kaplan-Moss',
    author_email = 'github@racklabs.com',
    packages = find_packages(exclude=['tests']),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = requirements,
    
    tests_require = ["nose", "mock"],
    test_suite = "nose.collector",
    
    entry_points = {
        'console_scripts': ['novatools = novatools.shell:main']
    }
)
