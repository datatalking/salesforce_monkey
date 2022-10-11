Salesforce Monkey

a simple tool to access your salesforce data

no more dealing with SQL.

conduct simple text based searches for marketing, sales or customer analystics

expand upon the work here, use sqlAlchemy for Django or Flask
# not all instances of salesforce will work with this prototype
    see future features
# links https://github.com/simple-salesforce/simple-salesforce
# https://github.com/simple-salesforce/simple-salesforce
# https://gist.github.com/rapatil/b269a347d50dc76b6fd29bec85889c28

# Required Packages
* tap-salesforce: a Singer tap to extract data from Salesforce. More info on GitHub.
* target-csv: a Singer target which converts input JSON data to CSV files. More info on GitHub. We’ll use the hotglue fork which uses updated dependencies.
* singer-discover: an open source utility to select streams from a Singer catalog. More info on GitHub.
* pandas: a widely used open source data analysis and manipulation tool. More info on their site and PyPi.
* gluestick: a small open source Python package containing util functions for ETL maintained by the hotglue team. More info on PyPi and GitHub.


# installation
setup.py salesforce_monkey

# Future Features
enable local elastic search
enable oracle dbase options


# Feature History
# https://stackoverflow.com/questions/30861524/logging-basicconfig-not-creating-log-file-when-i-run-in-pycharm