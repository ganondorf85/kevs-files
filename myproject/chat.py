import os
from socket import *
host =""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "waiting to recieve messages..."
while True:
	(data, addr) = UDPSock.recvfrom(buf)
	print "Recieved message: " + data if data == "exit":
		break
UDPSock.close()
os._exit(0)