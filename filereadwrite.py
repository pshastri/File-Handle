import sys
import os
import re

myFile=open("C:\\Users\\pshastri\\Desktop\\test.txt",'r')
mynewFile=open("C:\\Users\\pshastri\\Desktop\\newtest.txt",'w+')
myFilecont=myFile.read()

myFilecont=re.split('\s',myFilecont)


myWord="cloud"
for line_no,line in enumerate(myFilecont,0):

	
	mynewFile.write(line+"\n")
	if myWord.lower()==line.lower():
		
		mynewFile.write("is the next thing\n")
	
