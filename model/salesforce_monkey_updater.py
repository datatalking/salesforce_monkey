# FILENAME salesforce_updater.py
# SOURCE

from simple_salesforce import Salesforce
import os
import requests
from decouple import config


# Set environment variables
os.environ['SALESFORCE_API_USER'] = 'username'
os.environ['SALESFORCE_API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('SALESFORCE_API_USER')
PASSWORD = os.environ.get('SALESFORCE_API_PASSWORD')

# Getting non-existent keys
"""
FOO = os.getenv('FOO') # None
BAR = os.environ.get('BAR') # None
BAZ = os.environ['BAZ'] # KeyError: key does not exist.
"""

# TODO update for windows11 users sf = Salesforce(password='password', username='myemail@example.com')

# TODO update with https://medium.com/@koki_noda/historical-analysis-using-python-investment-strategies-as-the-fed-is-fighting-inflation-5f45516d11ea