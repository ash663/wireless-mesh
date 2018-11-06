import getIP
import os

SET_IP_CMD = 'sh setIP.sh'
SET_IP_MASK = '255.0.0.0'

def setIP():
	try	:
		os.system(SET_IP_CMD+' '+getIP.getIP()+' '+SET_IP_MASK)
		print("Your new IP address is: ",getIP.getIP())
	except Exception as e:
		print("Error :",e)

if __name__=='__main__':
	setIP()


