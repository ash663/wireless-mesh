import argparse
import setIP
import os


# Chnage here for MAC/UBUNTU
CREATE_SCRIPT_CMD='swift setup.swt'

parser = argparse.ArgumentParser(description='Create an AdHoc Network :)')
parser.add_argument('--essid',help='Your network ESSID',required=True)
parser.add_argument('--pass',help='Your network password',required=True)
parser.add_argument('--channel',help='Your network channel',required=True)
args = parser.parse_args()
args = vars(args)

BROADCAST_CMD =  'python keepPinging.py' #for ubuntu ;for all ???

try:

	# Create Network
	os.system(CREATE_SCRIPT_CMD+' '+args['essid']+' '+args['pass']+' '+args['channel'])

	print("Setting IP..")
	setIP.setIP()
	print("IP setup.. ")

	# BROADCAST
	os.popen(BROADCAST_CMD)
	print "BROADCAST DONE"

except Exception as e:
	print("Error:",e)




