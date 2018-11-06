# INTF='en0'
# for MACOSx and Ubuntu
# INTIALLY HUM APNI ARP TABLES CAHE DELETE KAR DENGE
# sudo arp -i 'en0' -a | grep -oh

import os
import getIP

# CHANGE HERE FOR MAC/UBUNTU
INTERFACE='en0'



nodes = os.popen('arp -i \''+INTERFACE+'\' -a | grep -o \'[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\'').read().strip().split('\n')

new =[]
for node in nodes:
 	# ping all nodes
 	if node!='':
		# -W 1 ==> wait max one sec
		ans = os.popen('ping -c 1 -W 1 '+node+' 2> /dev/null')
		ret = ans.close()

		if ret == None:
			# https://docs.python.org/2/library/os.html#os.popen
			# success
			new.append(node)
		else:
			# print("DELETING")
			ans = os.popen('sudo arp -d '+node+' 2> /dev/null')
			ret = ans.close()
			if ret == None :
				print(node+" : Entry Left(??) ")
			else:
				pass

print("Your neighbours are:")
for i in new:
	if i=='10.255.255.255':
		print i+" (BROADCAST)"
	elif i == getIP.getIP():
		print i+" (YOU)"
	else:
		print i



