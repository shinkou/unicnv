#!/usr/bin/env python
# vim: fenc=utf-8 ff=unix ft=python lcs=tab\:>. list noet sw=4 ts=4 tw=0
from setuptools import setup
import unittest

def unicnv_test_suite():
	test_loader = unittest.TestLoader()
	test_suite = test_loader.discover('tests', pattern = 'test_*.py')
	return test_suite

setup(
	name = 'unicnv'
	, version = '0.1'
	, packages = ['unicnv']
	, scripts = ['bin/unidoc-utf16']
	, author = 'Chun-Kwong Wong'
	, author_email = 'chunkwong.wong@gmail.com'
	, description = 'Unicode Official Document Converter'
	, url = 'https://github.com/shinkou/unicnv'
	, test_suite = 'setup.unicnv_test_suite'
)
