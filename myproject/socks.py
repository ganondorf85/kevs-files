import socket

hostname = raw_input("Enter host name: ")

hostIP = socket.gethostbyname(hostname)

print hostIP