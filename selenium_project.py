
#SELENIUM SCRIPT WRITING TO GOOGLE SHEETS

'''
SBC Automation SnoBird Report
Eric Nuno
8/30/2017
'''

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
	import argparse
	flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
	flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'C:\\Users\\gilliama\\Documents\\Python\\Scripts\\client_secret.json'
APPLICATION_NAME = 'Selenium'

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, datetime, os
from selenium.webdriver.support.ui import Select
import win32com.client as win32
from win32com.client import Dispatch
from pywintypes import TimeType


def get_credentials():

	"""Gets valid user credentials from storage.

	If nothing has been stored, or if the stored credentials are invalid,
	the OAuth2 flow is completed to obtain the new credentials.

	Returns:
		Credentials, the obtained credential.
	"""

	home_dir = os.path.expanduser('~')
	credential_dir = os.path.join(home_dir, '.credentials')
	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)
	credential_path = os.path.join(credential_dir,
								   'sheets.googleapis.com-python-quickstart.json')

	store = Storage(credential_path)
	credentials = store.get()
	if not credentials or credentials.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		flow.user_agent = APPLICATION_NAME

		if flags:
			credentials = tools.run_flow(flow, store, flags)
		else: # Needed only for compatibility with Python 2.6
			credentials = tools.run(flow, store)
		print('Storing credentials to ' + credential_path)
	return credentials

def Google_Sheets(data):  #was main()

	"""
	Shows basic usage of the Sheets API.

	Creates a Sheets API service object and prints the names and majors of
	students in a sample spreadsheet:
	https://docs.google.com/spreadsheets/d/15WIi-njEpTxvM8q9gVET_mQKrPIpxOUHluNtP1NbwQI/edit

	"""
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
					'version=v4')
	service = discovery.build('sheets', 'v4', http=http,
							  discoveryServiceUrl=discoveryUrl)

	spreadsheetId = '15WIi-njEpTxvM8q9gVET_mQKrPIpxOUHluNtP1NbwQI'
	rangeName = 'WIP Report!A1:M20000'
	values = []

	for info in data:
		values += [info] #same as appending

	body = {'values':values} #{"key":DataForThatKey}


	result = service.spreadsheets().values().update(
		spreadsheetId=spreadsheetId, range=rangeName, valueInputOption = 'RAW', body = body).execute()


def SBC_Excel():

	DIR = os.listdir('C:/users/gilliama/Downloads/')
	finalDir = ''
	newest = 0

	for d in DIR:
		if "wwt_wip" in d and "~" not in d:
			if os.path.getctime('C:/users/gilliama/Downloads/' + d) > newest:
				newest = os.path.getctime('C:/users/gilliama/Downloads/' + d)
				finalDir = 'C:/users/gilliama/Downloads/' + d

	print(finalDir)
	xlApp = Dispatch("Excel.Application")
	xlApp.Visible = True
	wb = xlApp.Workbooks.Open(finalDir)
	ws = wb.Sheets(1)

	LastRow = ws.UsedRange.Rows.Count
	LastColumn = 13

	data = []
	i = 1
	while i <= LastRow:

		z = 1
		columnData = []
		while z <= LastColumn:
			if ws.Cells(i,z).Value != None:
				if type(ws.Cells(i,z).Value) is TimeType:
					columnData.append(str(ws.Cells(i,z).Value))
				else:
					try:
						columnData.append(int(ws.Cells(i,z).Value))
					except:
						columnData.append(ws.Cells(i,z).Value)
			z+= 1
		data.append(columnData)
		i+=1
	wb.Close()
	Google_Sheets(data)
	return

def SnoBird():

	PasswordFile = open('C:/Users/gilliama//Desktop/Password.txt', 'r')
	Password = PasswordFile.read()
	PasswordFile.close()

	options = webdriver.ChromeOptions()
	#options.add_argument('headless')
	options.add_argument('window-size=1200x800')
	driver = webdriver.Chrome(chrome_options=options)

	driver.get('https://www.wwt.com/snobird/')

	driver.switch_to_frame(driver.find_element_by_id('content'))
	driver.switch_to_frame(driver.find_element_by_id('credentials'))

	driver.find_element_by_id('username').send_keys('lalonder')
	driver.find_element_by_id('password').send_keys(Password)

	driver.find_element_by_id('submit').click()

	time.sleep(3)

	driver.execute_script("javascript:addReportTab('https://reports.wwt.com/ibi_apps/WFServlet?IBIMR_action=MR_RUN_FEX&IBIMR_sub_action=MR_STD_REPORT&IBIMR_drill=RUNNID&IBIMR_fex=IBFS:/WFC/Repository/logistic/std_reports/reportsa75i8/shippingqs4b/WIP_status_report.htm&IBIMR_folder=%23shippingqs4b&IBIMR_domain=logistic/logistic.htm&P_REPORT_ID=23984&TARGET=_blank','SBC WIP Status Report');")

	time.sleep(65)



	driver.switch_to_frame(driver.find_element_by_id('iframe-1'))
	driver.find_element_by_id('radio3_2').click()

	driver.execute_script("javascript:OnExecute(null, 'image2')")
	#driver.close()


	SBC_Excel()

	return
#Google_Sheets()
#SBC_Excel()
SnoBird()
