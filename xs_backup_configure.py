#!/bin/python

import os,socket
execfile("py_helper/helper.py")


banner("Add CRONJOB")
currentpath=os.getcwd()
hostname=socket.gethostname()

if ask("Should we add an cronjob ? ")=="":
    
    path=ask("Witch Path ? Should we use " + currentpath  + "?  [Hit ENTER or type your path]   ")
    if path=="":
	path=currentpath
	
    when=ask("When to start backup [22:00] ?")
    if when=="":
	print("No time given!")
	exit(1)
    time=when.split(":")
	
    crontab=open("/var/spool/cron/root", "a")
    
    crontab.write( time[0]+ " " + time[1] +" 1-5 * * " + path + "/VmBackup/VmBackup.py " + path + "/pwd.file " + path + "/daily.cfg >> " + path + "/logs/" + hostname + ".log 2>&1\n")
    crontab.write( time[0]+ " " + time[1] +" 6 * * " + path + "/VmBackup/VmBackup.py " + path + "/pwd.file " + path + "/weekly.cfg >> " + path + "/logs/" + hostname + ".log 2>&1\n")
    crontab.close()
else:
    print("Skipped!")


