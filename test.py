import os, sys
import string

f = open('terms.txt', 'r')
lines = string.split(f.read(), '\n')
f.close

myTerms = []

for line in lines:
	if not line == '':
		myTerms.append(line)
	
print myTerms