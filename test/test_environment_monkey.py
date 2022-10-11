# FILENAME test_environment_monkey.py


import os
from simple_salesforce import Salesforce
import requests
import pandas as pd
from io import StringIO
import logging
from dotenv import load_dotenv


def main():
	test_environment_variables()
	test_environment_user()
	test_environment_security()
	test_environment_database()
	test_environment_self_similarity()
	test_environment_self_log()
	test_singer_taps()
	test_singer_targets()
	test_sfdc_version()
	test_sfdc_passed()


def test_environment_variables():
	"""
	print existing environment variables as list
	"""
	print("the os.environ = ", os.environ)


def test_environment_user():
	"""
	# TODO
	tests that the user is from an approved list
	:return:
	"""
	"""
	os.environ.get('USER')
		if os.environ.get('USER') == 'WADE':
			message.option == 'error':
			return print("I will log a message on a ERROR level"), logging.debug({message})
	"""

def test_environment_security():
	"""

	:return:
	"""
	print("test_environment_security function run")



def test_environment_database():
	"""

	:return:
	"""
	print("test_environment_database function run")


def test_environment_self_similarity():
	"""
	
	:return:
	"""
	print("test_environment_self_similarity function run")


def test_environment_self_log():
	"""
	
	:return:
	"""
	import logging
	
	message_option = {'debug', 'info', 'warning'
	                  'error', 'critical', 'basicConfig'}
	for message in message_option:
		if message_option == 'debug':
			print("I will log a message on a DEBUG level"), logging.debug({message.self})
		elif message_option == 'warning':
			print("I will log a message on a WARNING level"), logging.debug({message})
		elif message_option == 'error':
			print("I will log a message on a ERROR level"), logging.debug({message})
		elif message_option == 'critical':
			print("I will log a message on a CRITICAL level"), logging.debug({message})
		elif message_option == 'basicConfig':
			print("I will log a message on a BASICCONFIG level"), logging.debug({message})
		else:
			print("I will log a message on a NOERROR level"), logging.debug({message})
	
	logging.basicConfig(filename="SFDC_log.txt", level=logging.DEBUG)
	logging.basicConfig()
	# TODO fix singer log singer_log_history = append("SFDC_singer_log.txt")
	
	import logging
	
	# create logger
	logger = logging.getLogger("logging_tryout2")
	logger.setLevel(logging.DEBUG)
	
	# create console handler and set level to debug
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	
	# create formatter
	formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
	
	# add formatter to ch
	ch.setFormatter(formatter)
	
	# add ch to logger
	logger.addHandler(ch)
	
	print("singer_log_history updated")


def test_singer_taps():
	"""

	:return:
	"""
	springer_taps = {"3PL Central",
	                 "AdRoll",
	                 "Amazon S3 CSV Amplitude",
	                 "AppsFlyer",
	                 "Autopilot BigCommerce",
	                 "Bing Ads",
	                 "Braintree Bronto",
	                 "COVID-19 Public Data",
	                 "Campaign Manager Campaign Monitor",
	                 "Chargebee",
	                 "Chargify Close",
	                 "Club Speed",
	                 "Codat Dark Sky",
	                 "Deputy",
	                 "Dynamo DB Ebay",
	                 "Eloqua",
	                 "Exchange Rates API Facebook Ads",
	                 "Freshdesk",
	                 "Front FullStory",
	                 "GitHub",
	                 "GitLab Google Ads",
	                 "Google Analytics",
	                 "Google Analytics 360 Google Search Console",
	                 "Google Sheets",
	                 "Harvest Harvest Forecast",
	                 "Heap",
	                 "HubSpot IBM Db2",
	                 "Impact",
	                 "Intercom Invoiced",
	                 "Jira",
	                 "Klaviyo Kustomer",
	                 "Lever",
	                 "LinkedIn Ads Listrak",
	                 "LivePerson",
	                 "LookML Looker",
	                 "Mailshake",
	                 "Mambu Marketo",
	                 "Mixpanel",
	                 "MySQL Onfleet",
	                 "Oracle",
	                 "Outbrain Outreach",
	                 "Pardot",
	                 "Pendo Pepperjam",
	                 "Pipedrive",
	                 "Platform Purple PostgreSQL",
	                 "Quick Base",
	                 "Recharge Recurly",
	                 "Referral SaaSquatch",
	                 "Responsys Revinate",
	                 "SFTP",
	                 "SaaSOptics Salesforce",
	                 "Salesforce Marketing Cloud",
	                 "Selligent SendGrid Core",
	                 "ShipHero",
	                 "Shippo Shopify",
	                 "Slack",
	                 "Square Stripe",
	                 "SurveyMonkey",
	                 "Taboola Toggl",
	                 "Trello",
	                 "Typeform Urban Airship",
	                 "Uservoice",
	                 "Wootric Workday RaaS",
	                 "Xero",
	                 "Yotpo Zendesk Chat",
	                 "Zendesk Support",
	                 "Zoom Zuora",
	                 "iLEVEL"
	                 }


def test_singer_targets():
	"""
	
	:return:
	"""
	singer_targets = {
		"CSV",
		"Google BigQuery",
		"Google Sheets",
		"Keboola",
		"Magento BI",
		"PostgreSQL",
		"Rakam",
		"ReSci",
		"Stitch",
		"data.world"
	}


def test_sfdc_version():
	"""
	script to ensure proper version is being accessed, is available, varaibles are correct
	:return:
	"""
	# TODO manually changed, need a script for 3 releases
	# TODO create a script for v+1 version check
	sfdc_version_control = {
		"Winter '23 (v56.0)",
		"Summer '22 (v55.0)",
		"Spring '22 (v54.0)",
		"Winter '22 (v53.0)",
		"Summer '21 (v52.0)",
		"Spring '21 (v51.0)",
		"Winter '21 (v50.0)",
		"Summer '20 (v49.0)",
		"Spring '20 (v48.0)",
		"Winter '20 (v47.0)",
		"Summer '19 (v46.0)",
		"Spring '19 (v45.0)",
		"Winter '19 (v44.0)",
		"Summer '18 (v43.0)",
		"Spring '18 (v42.0)",
		"Winter '18 (v41.0)",
		"Summer '17 (v40.0)",
		"Spring '17 (v39.0)",
		"Winter '17 (v38.0)",
		"Summer '16 (v37.0)",
		"Spring '16 (v36.0)",
		"Winter '16 (v35.0)",
		"Summer '15 (v34.0)",
		"Spring '15 (v33.0)",
		"Winter '15 (v32.0)",
		"Summer '14 (v31.0)",
		"Spring '14 (v30.0)",
		"Winter '14 (v29.0)",
		"Summer '13 (v28.0)",
		"Spring '13 (v27.0)",
		"Winter '13 (v26.0)",
		"Summer '12 (v25.0)",
		"Spring '12 (v24.0)",
		"Winter '12 (v23.0)",
		"Summer '11 (v22.0)",
		"Spring '11 (v21.0)",
		"Winter '11 (v20.0)",
		"Summer '10 (v19.0)",
		"Spring '10 (v18.0)",
		"Winter '10 (v17.0)",
		"Summer '09 (v16.0)",
		"Spring '09 (v15.0)",
		"Winter '09 (v14.0)",
		"Summer '08 (v13.0)",
		"Spring '08 (v12.0)",
		"Winter '08 (v11.0)",
		"Summer '07 (v10.0)",
		"Spring '07 (v9.0)",
		"Winter '07 (v8.0)",
		"Summer '06 (v7.0)",
		"Spring '06 (v6.0)",  # NR
		"Winter '06 (v5.0)",
		"Summer '05 (v4.0)",  # NR
		"Spring '05 (v3.0)",
		"Winter '05 (v2.0)",
		"Summer '04 (v1.0)",
		"Spring '04 (v?.?)",
		"Winter '04 (v?.?)"
	}
	for version in sfdc_version_control:
		sfdc_version_control = "Summer '22 (v55.0)"
			# TODO add checking


def test_sfdc_passed():
	"""
	testing if sfdc passed append log
	:return:
	"""
	import logging
	logger = logging.getLogger()
	fhandler = logging.FileHandler(filename='SFDC_EVENT_log.log', mode='a')
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	logging.info("The program is working as expected")
	fhandler.setFormatter(formatter)
	logger.addHandler(fhandler)
	logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
	load_dotenv()
	singer_taps_list = dict
	singer_targets = dict
	singer_log_history = dict
	logging.basicConfig(
		filename='SFDC_HISTORY_listener.log',
		level=logging.DEBUG,
		format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S',
	)
	class message:
		def __init__(self, option_debug, option_info, option_warning, option_error, option_critical, option_basicConfig):
			self.debug = option_debug
			self.info = option_info
			self.warning = option_warning
			self.option = option_info
			self.error = option_error
			self.crtical = option_critical
			self.basicConfig = option_basicConfig
	communication = message(0, 0, 0, 0, 0, 0)
	main()
	message = ''
