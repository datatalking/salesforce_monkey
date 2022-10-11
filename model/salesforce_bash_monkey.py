# SOURCE https://stackoverflow.com/questions/13745648/running-bash-script-from-within-python
# TODO this when we need to run the script for AWS deployments
# FIXME

import subprocess
# some_file.py bash_script_maker
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/wadewilson/sbox/Toolbox_Code')
# import bash_script_maker

# from ToolBox_Code import bash_script_maker

def bash_script_sfdc_start_maker():
	"""
	bash script that create the python venv
	:return:
	"""
	# TODO if not exists
	with open('sfdc_start.sh', 'w') as rsh:
		rsh.write('''\
		#! /bin/bash
		echo "python3 -m venv ~/env/tap-salesforce"
		''')


def bash_script_sfdc_sleep_maker():
	"""
	bash script that create the python venv
	:return:
	"""
	# TODO if not exists
	with open('sfdc_sleep.sh', 'w') as rsh:
		rsh.write('''\
		#! /bin/bash
		echo "python3 -m venv  deactivate"
		''')


def download_install_gluestick():
	"""
	creates bash script to downlownd and install gluestick
	:return:
	"""
		# TODO if not exists
	with open('sfdc_sleep.sh', 'w') as rsh:
		rsh.write('''\
		#! /bin/bash
		echo "pip install tap-salesforce git+https://github.com/hotgluexyz/target-csv.git gluestick pandas ipykernel singer-python==5.3.1 https://github.com/chrisgoddard/singer-discover/archive/master.zip"
		''')


def create_python_env(bash_start, bash_script_name, bash_end):
	"""
	bash script to create the python venv
	:return:
	"""
	bash_start = str
	bash_script_name = str
	bash_end = str
	import subprocess

	# TODO 'if NOT exists source file_name.sh'

	for bash in bash_script_name:
		if bash_script_name == 1:
			print("I will now start the bash script {bash_script_name}")
			# bash_script_maker('python3 -m venv ~/env/tap-salesforce')
			subprocess.call("sfdc_start.sh")
		elif bash_script_name == 0:
			print("I will now end the bash script {bash_script_name}")
			subprocess.call("sfdc_sleep.sh")
		return

# TODO work up fix like this for windows11 users
# val = subprocess.check_call("./script.sh '%s'" % bash_start, shell=True)