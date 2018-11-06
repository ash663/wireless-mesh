import argparse
import os
import setIP
import getIP

parser = argparse.ArgumentParser(description='Join an AdHoc Network :)')
parser.add_argument('--essid',nargs=1,help='ESSID you want to Join')
parser.add_argument('--pass',nargs=1,help='Provide a password')
parser.add_argument('-l',action='store_true',help="List all Essids available")
args = parser.parse_args()
args = vars(args)



# Change here for MAC/UBUNTU
SHOW_ESSID_CMD = 'sh showESSID.sh'
JOIN_NW_CMD = 'sh join.sh'
GET_NEIGHBOUR_CMD = 'python getNeighbours.py'
BROADCAST_CMD =  'python keepPinging.py' #for ubuntu for all ???



# BROADCAST_CMD= 'sh PingOnce.sh' #for MACOsx

if args['l']:
	# List all essids 
	print "LISTING ALL ESSIDS"
	os.system(SHOW_ESSID_CMD)
else:
	summ = sum([1 if (args[i]!=None or args[i]!=False) else 0 for i in args])
	
	if summ == 0:
	 	# nothing specified
	 	parser.error('ESSID and PASS missing.... try python joinAdHoc.py -h')
 	elif (args['essid']!=None  and args['pass']!=None):
		print "JOINING NETWORK"
			
		# os.system('swift setup.swt')
		os.system(JOIN_NW_CMD+' '+args['essid'][0]+' '+args['pass'][0])
		
		print("Setting IP..")
		setIP.setIP()
		print("IP setup.. ")

		# BROADCAST
		os.popen(BROADCAST_CMD)
		print "BROADCAST DONE"
		
		
		print("Getting neighbours:")
		
		out = os.popen(GET_NEIGHBOUR_CMD)
		# COMMENT NEXT FOUR LINES AND SEE MAGIC HAPPEN
		for i in out:
			print "i in ",i
		# out.close()
		# print("out is ",out)
	

	else:
		if args['essid'] == None:
			parser.error('ESSID missing.... ')
		elif args['pass'] == None:
			parser.error('Password missing.... ')
