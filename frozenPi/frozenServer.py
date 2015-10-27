#!/usr/bin/env python
import socket, sys, picamera, datetime, fcntl, struct, shutil, os

#set SSH port for incoming connection
PORT = 8888

#Create socket
print 'Creating socket'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Getting pi number from static ip
print 'Isolating pi number determined from ip'
#Splitting ststic ip from eth0 field
ifname = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', 'eth0'[:15]))[20:24])
#Splitting last digit from ip adress with separator
temp,ifnum = ifname.rsplit('.', 1)
print 'Pi number is ' + ifnum

#Setting host ip adress
HOST = ifname

#Binding socket to host adress
print 'Binding Socket'
s.bind((HOST, PORT))
print 'Socket bind completed'

#Listen for incoming connections
s.listen(1)
print 'Socket listening'

#Infinite loop server starts here
while 1:
	#Start camera to haev it ready
	camera = picamera.PiCamera()
	#Flip image on camera
	camera.vflip = True
	#Accept and split incoming connection
	connection, adress = s.accept()
	print 'Connected with '+  adress[0] + ':' +  str(adress[1])
	#Extract data from connection
	data = connection.recv(1024)
	#Evaluate data and respond accordingly
	#If message is "FIRE" shoot camera X times
	if data == 'FIRE':
		try:
			#Capture image
			camera.capture('img'+ ifnum +'_1.jpg')
			shutil.copy('img'+ ifnum +'_1.jpg','/home/pi/frozenPi/pictures/')
			os.remove('img'+ ifnum +'_1.jpg')
			#camera.capture('img'+ ifnum +'_2.jpg')
			#camera.capture('img'+ ifnum +'_3.jpg')
			
		finally:
			#Close the camera to free it for the next fire command
			camera.close()
	if data == 'SHUTDOWN':
		#Close the camera to free it
		camera.close()
		#Close connection
		connection.close()
		#Close socket
		s.close()
		#Shutdown now
		os.system("poweroff")
		
	if data == 'ROLLCALL':
		print 'Ready!'
		#Close camera for next cycle
		camera.close()
	if not data:
		break
	#Close connection
	connection.close()
	print 'Connection with '+ adress[0] + ':' + str(adress[1]) +' closed'
#Close socket
s.close()
