import socket

IP = raw_input("Enter IP: ")

hostIP = socket.getfqdn(IP)

print hostIP