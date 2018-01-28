#!/usr/bin/python

import urllib

def read(file):
	open_file = open(file)
	contents = open_file.read()	
	open_file.close()
	return contents

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
	output = connection.read()
	connection.close()
	
	if "true" in output:
		print "Profanity check Failed!"
	elif "false" in output:
		print text
	else:
		print "Could not scan the document properly"

contents = read("index.html")
check_profanity(contents)
