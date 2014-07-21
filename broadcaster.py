import os
import subprocess
import commands

def send(user, passw, ip, category):
	get_ip = " ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}' "
	host_ip = commands.getoutput(get_ip)
	command = 'scp ' 
	args = '~/test.yeah' + user + '@' + ip + ':~/' + category
	
	process = subprocess.Popen(args.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
