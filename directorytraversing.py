import sys
import os


for root,dirs,files in os.walk("C:\\Users\\pshastri\\Documents\\GitHub\\Datastructures"):
	for myFile in files:
		print "This is a file: ", myFile
	for mydir in dirs:
		print "This is a Directory", mydir
	# print dirs
	# print files