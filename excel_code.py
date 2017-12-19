
#EXCEL CODE


import win32com.client as win32
from win32com.client import Dispatch
from time import sleep

'''pywin32 is an .exe file that can be found with a google search. It is required for this code to run.
it contains functions to run all windows office apps including the fuctions below using Excel and Outlook. Enjoy :)'''
def Main():

	xlApp = Dispatch("Excel.Application")
	xlApp.Visible = True

	wb = xlApp.Workbooks.Open('M:\\Network_repository\\_ITC Tools\\_Eric\\pythonTest.xlsx')
	ws = wb.Sheets(1)

	#print(ws.Cells(1,1).Value)
	#print(ws.Cells(1,2).Value)

	LastRow = ws.UsedRange.Rows.Count
	LastColumn = ws.UsedRange.Columns.Count

	i = 1

	while i <= LastRow:

		z = 1
		while z <= LastColumn:

			if ws.Cells(i, z).Value != None:
				if ws.Cells(i, z).Value == 'Mags':

					ws.Cells(i, z).Value = "Books"
					ws.Cells(i, z).interior.color = 2551530

				elif ws.Cells(i, z).Value == "Books":

					ws.Cells(i, z).Value = 'Mags'

			z += 1
		i += 1
	xlApp.DisplayAlerts = False

	wb.SaveAs('M:\\Network_repository\\_ITC Tools\\_Eric\\pythonTest.xlsx')

	xlApp.DisplayAlerts = True

	wb.Close()

	sleep(1)

	outlook = Dispatch('Outlook.Application')
	mail = outlook.CreateItem(0)
	mail.To = 'richard.lalonde@wwt.com'
	#mail.CC = '<email address>'
	#mail.BCC = '<email address>'
	mail.Subject = ''
	#mail.Body = 'string'
	#mail.Send = 'string'
	#mail.Attachments.Add = '<file path>'
	return

Main()
