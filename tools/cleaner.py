import sys
import commands
import os

if os.path.isfile('configs/%s' % sys.argv[1]) == False:
	print "config file not found"
	sys.exit(-1)

if os.path.isfile('../101logs/runner.log'):
	print "removind an old runner.log"
	os.remove('../101logs/runner.log')
   
config_file = open('configs/%s' % sys.argv[1], "r")
modules = config_file.readlines()

for module in modules:
	module = module.strip()	
	if module.__len__() < 2:
		continue

	commands.getstatusoutput('cd '+module+'; make clean')
	print "cleaning " + module
	if os.path.isfile("modules/"+module+'/pid'): 
		os.remove("modules/"+module+'/pid')
		print 'Removing PID...'
	if os.path.isfile("modules/"+module+'/module.log'):
		os.remove("modules/"+module+'/module.log')	
		print 'Removing log...'

sys.exit(0)
