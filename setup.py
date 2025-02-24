# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='django-regex-redirects',
    version='0.3.2a',
    author=u'Alex de Landgraaf',
    author_email='alex@maykinmedia.nl',
    packages=find_packages(),
    url='https://github.com/maykinmedia/django-regex-redirects',
    license='BSD licence, see LICENCE.txt',
    description='Django redirects, with regular expressions',
    include_package_data=True,
)
