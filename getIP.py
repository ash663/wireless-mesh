# FOR MAC/UBUNTU
from uuid import getnode as get_mac
# string = "08:00:27:1c:89:51"

def getIP():
	MAC = get_mac()

	#Convert number into  "08:00:27:1c:89:51" form
	MAC_HEX = ':'.join(("%012X" % MAC)[i:i+2] for i in range(0, 12, 2))

	array  = MAC_HEX.split(":")
	ip="10"
	array = array[3:]

	for i in array:
		j = str(int(str(i),16))
		ip= ip+"."+j

	return ip


