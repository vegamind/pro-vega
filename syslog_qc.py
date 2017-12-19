
#SCRIPT TO READ LOG FILES (CRITICAL ERRORS) FOR QC

import os

def main(): #change later

	path = "C:\\Users\\gilliama\\Desktop\\"  #insert path to file here

	f = open(path + "test.LOG", "r")

	read = f.read()
	read = read.replace("\x08", "")
	readLines = read.split("\n")
	#print(readLines)

	errorLog = []

	if "show inventory" not in read.lower():
		errorLog.append("show inventory is missing.")


	if "show environment" not in read.lower():
		errorLog.append("show environment is missing.")

	elif "show environment" in read.lower():
	#start looking at LED Information and end at BMC  Information
		startEnv = "LED Information"
		endEnv = "BMC  Information"
		startInt = 0
		endInt = 0
		i = 0
		while i < len(readLines):
			if startEnv in readLines[i]:
				startInt = i
			if endEnv in readLines[i]:
				endInt = i
			i = i + 1

		envChunk = readLines[startInt : endInt]
		#print(envChunk)

		envChunkStr = ""

		for line in envChunk:
			envChunkStr += (line).replace("\t", "")
		envChunkSplit = envChunkStr.split("0/RSP1/*")
		envRSP0 = envChunkSplit[0]
		envRSP1 = envChunkSplit[-1]

		#print (envRSP0.replace(" " , "").replace("\t",""))

		if "Critical-AlarmOff" not in envRSP0.replace(" " , ""):
			errorLog.append("Critical Alarm not in state of Off for RSP0.")

		if "Major-AlarmOff" not in envRSP0.replace(" ", ""):
			errorLog.append("Major Alarm not in state of Off for RSP0.")

		if "Minor-AlarmOff" not in envRSP0.replace(" ", ""):
			errorLog.append("Minor Alarm not in state of Off for RSP0.")

		if "ACOOff" not in envRSP0.replace(" ", ""):
			errorLog.append("ACO not in state of Off for RSP0.")

		if "FailOff" not in envRSP0.replace(" ", ""):
			errorLog.append("Fail not in state of Off for RSP0.")

		if "Critical-AlarmOff" not in envRSP1.replace(" " , ""):
			errorLog.append("Critical Alarm not in state of Off for RSP1.")

		if "Major-AlarmOff" not in envRSP1.replace(" ", ""):
			errorLog.append("Major Alarm not in state of Off for RSP1.")

		if "Minor-AlarmOff" not in envRSP1.replace(" ", ""):
			errorLog.append("Minor Alarm not in state of Off for RSP1.")

		if "ACOOff" not in envRSP1.replace(" ", ""):
			errorLog.append("ACO not in state of Off for RSP1.")

		if "FailOff" not in envRSP1.replace(" ", ""):
			errorLog.append("Fail not in state of Off for RSP1.")

	if "show diag summary" not in read.lower():
		errorLog.append("show diag summary is missing.")

	if "show diag detail" not in read.lower():
		errorLog.append("show diag detail is missing.")

	if "show version" not in read.lower():
		errorLog.append("show version is missing.")

	elif "show version" in read.lower():
		startVer = "show version"
		endVer = "admin show platform"
		startInt = 0
		endInt = 0
		i = 0
		while i < len(readLines):
			if startVer in readLines[i]:
				startInt = i
			if endVer in readLines[i]:
				endInt = i
			i = i + 1

		verChunk = readLines [startInt : endInt]

		verChunkStr = ""

		print(startInt, endInt)
		#print(verChunk)
		for line in verChunk:
			verChunkStr += (line)

		if verChunkStr.count("5.3.3") != 380:
			errorLog.append("Did not find expected amount of 5.3.3 files.")

		#print(verChunkStr.count("5.3.3"))








	if "admin show platform" not in read.lower():
		errorLog.append("admin show platform is missing.")

	if "admin show install" not in read.lower():
		errorLog.append("admin show install is missing.")

	if "admin show install active" not in read.lower():
		errorLog.append("admin show install active is missing.")

	if "admin show install committed" not in read.lower():
		errorLog.append("admin show install committed is missing.")

	if "show controllers epm-switch port-status 54 loc 0/rsp0/cpu0" not in read.lower():
		errorLog.append("show controllers epm-switch port-status 54 loc 0/rsp0/cpu0 is missing.")

	if "show controllers epm-switch port-status 55 loc 0/rsp0/cpu0" not in read.lower():
		errorLog.append("show controllers epm-switch port-status 55 loc 0/rsp0/cpu0 is missing.")

	if "show controllers epm-switch port-status 54 loc 0/rsp1/cpu0" not in read.lower():
		errorLog.append("show controllers epm-switch port-status 54 loc 0/rsp1/cpu0 is missing.")

	if "show controllers epm-switch port-status 55 loc 0/rsp1/cpu0" not in read.lower():
		errorLog.append("show controllers epm-switch port-status 55 loc 0/rsp1/cpu0 is missing.")

	if "term len 0" not in read.lower():
		errorLog.append("term len 0 is missing.")

	if "admin show hw-module fpd location all" not in read.lower():
		errorLog.append("admin show hw-module fpd location all is missing.")



	#for missing in errorLog:

		#print(missing)



	return


main()

"""

1. Check for show inventory
                2. Check for show environment
                                a. Verify there are no major alarms showing
                3. Check for show diag summary
                4. Check for show diag detail
                5. Check for show version
                                a. all listed codes need to show version 5.3.3 check each pie file
                6. Check for admin show platform
                                a. Make sure state is IOS XR RUN or READY, nothing else is acceptable
                7. Check for admin show install
                                a. Check that version 5.3.3 is installed
                                b. Must see additional packages disk0:asr9k-px-5.3.3.CSCuz84486-1.0.0 and disk0:asr9k-px-5.3.3.sp4-1.0.0
                8. check for admin show install active
                                a. Check that version 5.3.3 is installed
                                b. Must see additional packages disk0:asr9k-px-5.3.3.CSCuz84486-1.0.0 and disk0:asr9k-px-5.3.3.sp4-1.0.0
                9. Check for admin show install committed
                                a. Check that version 5.3.3 is installed
                                b. Must see additional packages disk0:asr9k-px-5.3.3.CSCuz84486-1.0.0 and disk0:asr9k-px-5.3.3.sp4-1.0.0
                10. Check for show controllers epm-switch port-status 54 loc 0/rsp0/cpu0
                11. Check for show controllers epm-switch port-status 55 loc 0/rsp0/cpu0
                12. Check for show controllers epm-switch port-status 54 loc 0/rsp1/cpu0
                13. Check for show controllers epm-switch port-status 55 loc 0/rsp1/cpu0
                14. Check for term len 0
                15. Check for admin show hw-module fpd location all
                                a. upgrade downgrade says "no" for upgrade

"""
