#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-addthis',
    version='2.0.1',
    author='Raymond Wanyoike',
    author_email='raymond.wanyoike@gmail.com',
    url='https://github.com/raymondwanyoike/django-addthis/',
    description='Simple integration of the AddThis social sharing widget in Django projects.',
    long_description=open('README.rst').read(),
    download_url='https://github.com/raymondwanyoike/django-addthis/',
    license='GPLv3',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)
