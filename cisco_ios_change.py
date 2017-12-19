
#SCRIPT TO AUTO CHECK OS & UPGRADE/DOWNGRADE OS OF CISCO ROUTERS

import sys


##crt.Sleep = milliseconds ex. 1000 = 1 second
##crt.Screen.WaitForString = seconds ex. 1 = 1 second

##This script checks where you are at in secureCRT Terminal and then checks the iOS and if the gps file is on the router.
def InstallIOS(CorrectIOS, NewBinCheck):

	crt.Screen.Send("config t\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("interface gigabitethernet 0\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("ip address 192.168.1.1 255.255.255.0\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("no shut\n")
	crt.Screen.WaitForString("GigabitEthernet0, changed state to up", 10)
	crt.Screen.Send("end \n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("copy tftp://192.168.1.2/" + CorrectIOS + " flash:\n\n\n\n")
	IOSSuccessful = crt.Screen.WaitForString("[OK - ", 900)

	if IOSSuccessful != 1:
		crt.Screen.Send("\x03")
		crt.Sleep(1000)
		crt.Screen.Send("copy tftp://192.168.1.2/" + CorrectIOS + " flash:\n\n\n\n")
		IOSSuccessful = crt.Screen.WaitForString("[OK - ", 900)
		if IOSSuccessful != 1:
			crt.Screen.Send("!!!!!!!!!!!!!!!!!!!!!\n")
			crt.Screen.Send("!!!Transfer Failed. Exiting Script.!!!\n")
			crt.Screen.Send("!!!!!!!!!!!!!!!!!!!!!\n")
			return("return")

	crt.Screen.Send("delete flash:" + NewBinCheck[0] + "\n\n\n\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("copy tftp://192.168.1.2/ratmgps_geof01.tcl flash: \n\n")
	crt.Screen.WaitForString("[OK - ")



	crt.Screen.Send("reload \n")
	crt.Screen.WaitForString("modified", 5)
	crt.Screen.Send("no \n\n\n")
	crt.Screen.WaitForString("System Configuration Dialog", 900)
	crt.Screen.Send("no \n")
	crt.Screen.WaitForString(">")
	crt.Screen.Send("en \n")
	crt.Screen.WaitForString("#")

	CheckForIOS()

	return


def Quality():

	crt.Sleep(1000)

	## This section for logging later
	# Log Here
	saveLocation = "M:/network_repository/output.txt"

	crt.Session.LogFileName = saveLocation

	crt.Session.Log(True)

	crt.Screen.Send("conf t \n")
	crt.Screen.WaitForString("(#")
	crt.Screen.Send("no service config \n")
	crt.Screen.WaitForString("(#")
	crt.Screen.Send("end \n")
	crt.Screen.WaitForString("#")
	crt.Sleep(2000)
	crt.Screen.Send("show version \n")
	crt.Screen.WaitForString("#")
	crt.Sleep(3000)
	crt.Screen.Send("show run \n")
	crt.Screen.WaitForString("#")
	crt.Sleep(10000)
	crt.Screen.Send("show env \n")
	crt.Screen.WaitForString("#")
	crt.Sleep(5000)
	crt.Screen.Send("dir flash: \n")
	crt.Screen.WaitForString("#")
	crt.Sleep(2000)
	crt.Screen.Send("show cell 0 hard \n")
	crt.Screen.WaitForString("#")
	crt.Sleep(3000)
	crt.Screen.Send("show cell 0 all \n")
	crt.Screen.WaitForString("#")
	crt.Sleep(3000)
	crt.Screen.Send("copy run start \n\n")
	crt.Screen.WaitForString("#")
	crt.Sleep(2000)
	crt.Screen.Send("!!! ARGP !!! \n")
	crt.Screen.WaitForString("#")


	crt.Session.Log(False)

	return


def CheckForIOS():

	CorrectIOS = "c800-universalk9-mz.SPA.156-2.T1.bin"

	crt.Screen.Send("term len 0\n")
	crt.Screen.WaitForString("#")

	crt.Screen.Send("dir | include .bin \n")
	crt.Screen.WaitForString("#")

	## This captures the last 2 rows of data from secureCRT.
	nRow = crt.Screen.CurrentRow
	StringBinCheck = crt.Screen.Get(nRow-4,0,nRow,132)

	#crt.Sleep(2000)

	## This is to force the unicode to a string
	StringBinCheck = str(StringBinCheck)
	#crt.Dialog.MessageBox(str(StringBinCheck))

	BinCheck = BinCheck.split(" ")

	#crt.Dialog.MessageBox(str(BinCheck))

	NewBinCheck = []

	for file in BinCheck:
		if ".bin" in file and ".bin" != file:
			crt.Dialog.Messagebox(NewBinCheck)
			NewBinCheck.append(file)


	StringBinCheck = StringBinCheck.replace("include.bin", "")


	if ".bin" == NewBinCheck:
		NewBinCheck.remove(".bin")


	if len(NewBinCheck) > 1:

		crt.Dialog.MessageBox("Detected multiple iOS files. Please delete pre-existing iOS. Exiting Script. Re-run once complete.")

	return("return")


	if CorrectIOS not in NewBinCheck:

		crt.Screen.Send("!!!!!!!!!!!!!!!!!!!!\n")
		crt.Screen.Send("!!Could not find IOS, adding IOS!!\n")
		crt.Screen.Send("!!!!!!!!!!!!!!!!!!!!\n")

		InstallIOS(CorrectIOS, NewBinCheck)

	else:
		crt.Screen.Send("!!!!!!!!!!!!!!!!!!!!\n")
		crt.Screen.Send("!!Found IOS, continuing with quality!!\n")
		crt.Screen.Send("!!!!!!!!!!!!!!!!!!!!\n")

		crt.Sleep(1000)

		crt.Screen.Send("dir | include.tcl \n")
		crt.Screen.WaitForString("#")
		nRow = crt.Screen.CurrentRow
		tclCheck = crt.Screen.Get(nRow-4, 0, nRow, 132)
		tclCheck = str(tclCheck)


		tclList = []
		tclCheck = tclCheck.split(" ")
		for tcl in tclCheck:
			if ".tcl" in tcl and ".tcl" != tcl:
				tclList.append(tcl)


		Quality()



	return


## This function finds where we are in the router and gets us back to enable mode.
def WhereAmI():

	## This sends 3 enters.
	crt.Screen.Send("\r\n\r\n\r")
	crt.Screen.Sent("en\n\n\n")

	## Here we are sleeping a second so that the script waits on the device.
	crt.Sleep(1000)

	## This captures the last 2 rows of data from secureCRT.
	nRow = crt.Screen.CurrentRow
	WhatIn = crt.Screen.Get(nRow-2,0,nRow,132)

	## Turning the content from unicode to standard UTF-8 string
	WhatIn = str(WhatIn)

	## Splitting up the string by spaces
	WhatIn = WhatIn.split(" ")

	NewWhatIn = []

	for what in WhatIn:
		if '' != what:
			NewWhatIn.append(what)

	if ">" in NewWhatIn [-1]:
		crt.Sreen.Send("en \n")
	## if we are in any configuration mode at all, it will have a )#
	elif ")#" in NewWhatIn [-1]:
		crt.Screen.Send("end \n")

	## Just checking what is returned
	#crt.Dialog.MessageBox(str(NewWhatIn))

	return


def Main():

	WhereAmI()
	ErrorExit = CheckForIOS()

	if ErrorExit == "return":
		return

	return

Main()
