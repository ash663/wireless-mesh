# for MAC/Ubuntu
import time 
import os
now = time.time()

while True:	
	if time.time()-now > 3:
		os.system('sudo ping -c 3 10.255.255.255')
		now = time.time()
