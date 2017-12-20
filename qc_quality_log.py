#FUNCTION TO CREATE TXT FILE W/UNIQUE NAME AND STORE LIST OF FILE STRUCTURE OF
#REPOSITORY - AUTO AUDIT OF FOLDER STRUCTURE

import os, time
'''
def qcLogOutput():
    dateTime = time.strftime("%m-%d-%y" + " %H-%M" + ".txt")
    fileName = open(dateTime, 'w')
    #variable for inputing text and then writing the text to that file
    fileName.close()
    #for loop to take list and write to text file


    return

qcLogOutput()
'''

path = 'C:\\Users\\gilliama\\Documents\\TEST Repository'

def projExe():
for folders in os.walk(path):
    if not os.path.exists('Project Execution Documentation'):
        #email me

'''
for path, dirs, files in os.walk(path):
    print(path)
    for f in files:
        print (f)
'''


#print(os.walk('C:\\Users\\gilliama\\Documents\\TEST Repository'))

#this script checks for proper hierchy of files in repository
#auto audit of folder structure
