# FILENAME test_salesforce_monkey.py
# SOURCE https://developer.salesforce.com/blogs/2021/09/how-to-automate-data-extraction-from-salesforce-using-python


from io import StringIO
from simple_salesforce import Salesforce
import pandas as pd
import requests
from dotenv import load_dotenv
# TODO fix pycrunch IDE disabled
#  import pycrunch-engine


def test_salesforce_report():
	sf_instance = 'https://oneappexchange.lightning.force.com/'  # Your Salesforce Instance URL
	reportId = ''  # add report id
	export = '?isdtp=p1&export=1&enc=UTF-8&xf=csv'
	sfUrl = sf_instance + reportId + export
	response = requests.get(sfUrl, headers=sf.headers, cookies={'sid': sf.session_id})
	download_report = response.content.decode('utf-8')
	df_sfdc_report = pd.read_csv(StringIO(download_report))



def main():
	test_some_script()
	test_trace_str_variable()
	test_trace_int_variable()
	test_salesforce_report()
	test_salesforce_field_names()


def test_some_script():
	import time
	from datetime import datetime
	import numpy as np
	
	count = 0
	while True:
		current_time = datetime.now()
		rng = np.random.default_rng()
		random_integers = rng.integers(low=0, high=10 ** 6, size=3)
		print(f"{current_time}: {random_integers}")
		count += 1
		if count == 10:
			print(f"Script completed")
			break
		time.sleep(5)


def test_trace_str_variable():
	"""
	test that strings as input are strings
	:return:
	"""

	random = ''
	words = ''
	random_words = random + '_' + words
	trace(my_dictionary=dict(a=random, b=words, sum=random_words))
	

def test_trace_int_variable():
	"""
	test that int as input are int
	:return:
	"""
	print("test_trace_int_variable function run")


def test_salesforce_report():
	sf_instance = 'https://oneappexchange.lightning.force.com/'  # Your Salesforce Instance URL
	reportId = ''  # add report id
	export = '?isdtp=p1&export=1&enc=UTF-8&xf=csv'
	sfUrl = sf_instance + reportId + export
	response = requests.get(sfUrl, headers=sf_instance.headers, cookies={'sid': sf_instance.session_id})
	download_report = response.content.decode('utf-8')
	df_sfdc_report = pd.read_csv(StringIO(download_report))


def test_salesforce_field_names():
	# check all field names of the object
	description_test = sf.UserInstall__c.describe()
	print([field['name'] for field in description_test['fields']])


if __name__ == "__main__":
	load_dotenv()
	# connect to Salesforce API using your credentials, you can use environment variables to protect your passwords
	sf_conn_test = Salesforce(username='SALESFORCE_API_USER',
	                         password='SALESFORCE_API_PASSWORD',
	                         security_token='SALESFORCE_API_TOKEN',
	                         subdomain='test')
	
	sf_conn = Salesforce(username='SALESFORCE_API_USER',
	                password='SALESFORCE_API_PASSWORD',
	                security_token='SALESFORCE_API_TOKEN')

	main()
	
	# TODO centralize PATH to .env
		# dotenv_path = Path('path/to/.env')
		# load_dotenv(dotenv_path=dotenv_path)
	# TODO add active_users, old_users to database for logging CYBERSEC
	# TODO expand on pytest testing
		# TODO expand on pycrunch https://pycrunch.com
	# TODO add more tests https://gist.github.com/rapatil/b269a347d50dc76b6fd29bec85889c28

