#FUNCTION TO CREATE TXT FILE W/UNIQUE NAME AND STORE LIST OF FILE STRUCTURE OF
#REPOSITORY - AUTO AUDIT OF FOLDER STRUCTURE
import os
import time

def qcLogOutput():
    dateTime = time.strftime("%m-%d-%y" + " %H-%M" + ".txt")
    fileName = open(dateTime, 'w')
    #variable for inputing text and then writing the text to that file
    fileName.close()
    #for loop to take list and write to text file


    return

qcLogOutput()


#this script checks for proper hierchy of files in repository
#auto audit of folder structure

#challenge create script to compare lists of folders in root folder, if one goes
#missing, email me, look at dir and list, then wait a few mins, check again and
#compare
