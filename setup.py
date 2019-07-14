try:
	from setuptools import setuptools

execpt ImportError:
	from distutils.core import setup

config = [
	'description': 'This project aims to offer helpful analysis of chess games',
	'author': 'Jan Janacek',
	'url': '',
	'version': '1.0'
]

setup(**config)

