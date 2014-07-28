import os
import subprocess
import commands

def update(data):
	args =  './update.sh ' + data
	process = subprocess.Popen(args.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]


f = open('credentials.txt')
for line in f:
	update(line)
