# PyScanner

This is a simple port scanner application in Python, the program is provided as it is and without any warranty so please use it at your own risk.

## Requirements

1. Python version **3**

## USAGE

From command line type the following inside the folder of the PyScanner

**python3 pyscanner.py 10.0.1.8 -p0-135**

The above command will scan the range of port from 0 to 135 for the ip 10.0.1.8

**python3 pyscanner.py 10.0.1.8 -p135**

The above command will scan the port 135 for the ip 10.0.1.8

## SAMPLE OUTPUT

------------------------------------------------------------
Please wait, scanning remote host 10.0.1.8
------------------------------------------------------------


 Port 135: 	 Open
 
 Port 139: 	 Open
 
 Port 445: 	 Open
 
 Port 554: 	 Open
 


Scanning Completed in:  0:00:00.588385

## CONTRIBUTE

The project can be successful if more people contribute to this project. If you have any idea you want to implement or think that there is a better way to implement any part of the code please create a pull request and I will do my best to merge appropriately.
