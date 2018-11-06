import argparse
import os

parser = argparse.ArgumentParser(description='Create an AdHoc Network :)')
parser.add_argument('-r',action='store_true',help="Recieve")
parser.add_argument('-s',action='store_true',help="Send")
args = parser.parse_args()
args = vars(args)


GET_NEIGHBOUR_CMD = 'python getNeighbours.py'
RECEIVE_FILE_CMD = 'python editFile.py'
SEND_FILE_CMD = 'python send.py'


if args['r']:
	# Receiving
	os.system(RECEIVE_FILE_CMD)
elif args['s']:
	# Send
	print
	print("You can send to following neighours : ")		
	out = os.popen(GET_NEIGHBOUR_CMD)
	for i in out:
		print "i in ",i,
	print
	os.system(SEND_FILE_CMD)


else:
	parser.error('You didn\'t specify what? .. Try `python transfer.py -h`')

