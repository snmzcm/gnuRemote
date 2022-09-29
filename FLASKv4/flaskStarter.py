import os
import socket   
#Finding Internal Ip
def findInternalIp():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)   
    print("Your Computer IP Address is:"+IPAddr)
    return  IPAddr
#-----
#Finds path
currentPath = os.path.abspath(os.getcwd())
print(currentPath)
#runs flask
def runFlask(IPAddr):
    flaskRunner = f'flask run -h {IPAddr} --port 80'
    os.system(f'cmd /k "{flaskRunner}"')

def startFlaskServer():
    IPAddr = findInternalIp()
    runFlask(IPAddr)


class flaskStarter:
    'pass'
    pass





