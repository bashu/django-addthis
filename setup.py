#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-addthis',
    version='2.0.0',
    description='Simple integration of the AddThis social sharing widget in Django projects.',
    author='Raymond Wanyoike',
    author_email='raymond.wanyoike@gmail.com',
    long_description=open('README.rst').read(),
    url='https://github.com/raymondwanyoike/django-addthis/',
    packages=find_packages(),
    include_package_data=True,
    keywords='django, addthis',
    install_requires=[
        'Django>=1.4,<=1.6.5',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    zip_safe=False,
)
