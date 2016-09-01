import sys
import os
import re

myFile=open("C:\\Users\\pshastri\\Desktop\\test.txt",'r')
myFilecont=myFile.read()
myFilecont=re.split('\s',myFilecont)

#print myFilecont
myWord="cloud"
for line in myFilecont:
	if myWord.lower()==line.lower():
		print "Found"