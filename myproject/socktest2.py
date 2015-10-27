import socket
import sys
import datetime

remoteServer = "localhost"

remoteServerIP = socket.gethostbyname(remoteServer)

print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" *60
for x in range (7000,9000):
	port=x


	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print "port {}: \t open".format(port)
		sock.close()

	except socket.gaierror:
		print 'hostname could not be resolved. exititng'
		sys.exit

	except socket.error:
		print "couldn't connect to server"
		sys.exit()