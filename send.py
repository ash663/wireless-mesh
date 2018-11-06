import os
destination=[]
ip = []
host="adhoc"
#n = input("Enter number of trusted machines")

'''def login(destination):
    #value=os.system("rlogin -l "+host+" "+destination)
    value=0
    if value == 0:
        return True
    else:
        return False
'''

'''if n>0:
    print "Enter IP addresses of trusted machines"
    for i in range(0, n):
        ip.append(raw_input())
    os.system("touch .rhosts")
    f=open('.rhosts', 'w+')
    f=open('.rhosts', 'a')
    for i in ip:
        f.write(i)
else:
    print "Trust no man"'''


#fileName = raw_input("Which file to transfer?\n")
numDestination = input("Number of destinations: \n")

#if numDestination==1:
for i in range(0, numDestination):
    content = []
    destination = raw_input("Transfer destination: \n")
    os.system("rm details.txt")
    os.system("cat askReceiverPort.txt - | nc "+destination+" 10000 > details.txt")
    with open("details.txt") as f:
        content = f.readlines()
    #print content
    #if login(destination):
    #if os.path.isfile(content[1]):
    print "scp "+content[1].strip()+" "+host+"@"+destination+"://Users/"+host
    os.system("scp "+content[1].strip()+" "+host+"@"+destination+"://Users/"+host)
            #os.system("pv -p -r "+content[1]+" | nc -w 10 "+destination+" "+content[0])
    #else:
    #    print "Unauthorized"






'''if numDestination>0 and numDestination==1:
    destination = raw_input("Transfer destination(s): \n")
    login()
    result = os.system("pv -p -r "+fileName+"| nc -w 10 "+destination+" 10000")
    #else:
    #    print "Unauthorized"
elif numDestination>1:
    for i in range(0, numDestination):
        dest = raw_input("Destination "+i)
        os.system("rlogin -l "+host+" "+dest):
        os.system("pv -p -r "+fileName+"| nc -w 10 "+dest+" 10000")
        #else:
        #    print "Unauthorized"'''
