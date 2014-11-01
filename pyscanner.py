#!/usr/bin/env python3

# This is a simple port scanner application in Python,
# the program is provided as it is and without any warranty
# so please use it at your own risk.

# USAGE

##################################################
# python3 pyscanner.py 10.0.1.8 -p0-135 ########## 
##################################################

# the above command will scan the range of port from 0 to 135 for the ip 10.0.1.8


################################################
# python3 pyscanner.py 10.0.1.8 -p135 ##########
################################################

# the above command will scan the port 135 for the ip 10.0.1.8

##########################
# SAMPLE OUTPUT ##########
##########################
# ------------------------------------------------------------
# Please wait, scanning remote host 10.0.1.8
# ------------------------------------------------------------
#
#
# Port 135: 	 Open
# 
# Port 139: 	 Open
#
# Port 445: 	 Open
#
# Port 554: 	 Open
# 
#
#
# Scanning Completed in:  0:00:00.588385



# Import required modules
import socket
import sys
import re
from datetime import datetime

# Convert HostName to IPv4 address
remoteServerIP  = socket.gethostbyname(sys.argv[1])

# Print a nice banner with information on which host we are about to scan
print("\n")
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)
print("\n")

# Check what time the scan started
t1 = datetime.now()

#if pattern:
#	start, end = pattern.group()[2:].split("-")
#	print(start)
#	print(end)
#else:
#	port = portsArg[2:]

try:
	# Take the second arguement as the port number range or just a specific port
	portsArg = sys.argv[2]

	# Searches for a specific pattern in the second arguement for port range -p0-1024
	pattern = re.search('^-p[0-9]*-[0-9]*', portsArg)

	portsFound = False

	if pattern:
		start, end = pattern.group()[2:].split("-")
		start = int(start)
		end = int(end)+1
		for port in range(start,end):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((remoteServerIP, port))
			if result == 0:
				print('\033[92m',"Port %d: \t Open\n" %port, '\033[0m')
				portsFound = True
			sock.close()
	else:
		port = int(portsArg[2:])
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print('\033[92m',"Port %d: \t Open\n" %port, '\033[0m')
			portsFound = True
		sock.close()
	if portsFound == False:
		print('\033[92m',"No ports open", '\033[0m')

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print("\n")
print('Scanning Completed in: ', total)
print("\n")

