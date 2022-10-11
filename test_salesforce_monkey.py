# FILENAME test_salesforce_monkey.py


import os


def test_environment_variables():
	"""
	print existing environment variables as list
	"""
	print(os.environ)


def test_environment_user():
	os.environ.get('USER')