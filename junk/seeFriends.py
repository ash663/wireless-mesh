import os 
import getIP
GET_NEIGHBOUR_CMD = 'python getNeighbours.py'

try : 
	print("Your IP address is ",getIP.getIP())
	ans = os.popen(GET_NEIGHBOUR_CMD	)	
	for i in ans:
		print i,	
except Exception as e:
	# print("Exception :",e)
	pass

