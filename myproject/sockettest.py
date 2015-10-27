import socket

remoteServer = "localhost"

remoteServerIP = socket.gethostbyname(remoteServer)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex((remoteServerIP, 23))

print "response = " +str(result)

if result == 0:
	print "port open"

if result == 111:
	print "port closed"

sock.close()