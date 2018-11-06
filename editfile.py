import re
import os

os.system("nc -l 10000")

# portno = 30000
# input_file=open("/etc/ssh/sshd_config","w+")
# p=re.compile('Port [0-9]+')
# for line in input_file:
#         if p.match(line.strip()):
#             output_file.write('Port '+ portno)
