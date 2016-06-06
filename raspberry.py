import socket   #for sockets
import sys  #for exit

import serial #for ttlUSB0
import time #for delay

sbuf = 0
t1temp1=0
t1temp2=0
t1temp3=0
t2temp=0
t3temp=0 
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 0.5)  #start USB->TTL

try:
    #create an AF_INET, STREAM socket (TCP)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	sys.exit();
 
print 'Socket Created'

host = 'tcp.lewei50.com'
port = 9960
userkey='b40abe71193d4211946a6662b0908860'
sensor1='T1'
sensor2='T2'
sensor3='T3'

try:
	remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
	print 'Hostname could not be resolved. Exiting'
	sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip

s.connect((remote_ip , port)) 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip

while True:
	for sbuf in range(5):
		if ser.isOpen() == False:
			ser.open()
		ser.write(chr(sbuf))
		try:
			re = ser.readlines()
		except:
			pass
		if sbuf == 0:
			t1temp1=ord(re[0])
		if sbuf == 1:
			t1temp2=ord(re[0])
		if sbuf == 2:
			t1temp3=ord(re[0])
		if sbuf == 3:
			t2temp=ord(re[0])
		if sbuf == 4:
			t3temp=ord(re[0])
		time.sleep(1)
	print t1temp1,t1temp2,t1temp3,t2temp,t3temp
	
	message = "{\"method\": \"update\",\"gatewayNo\": \"01\",\"userkey\": \""+userkey+"\"}&^!"
	 
	try :
		#Set the whole string
		s.sendall(message)
	except socket.error:
		#Send failed
		print 'Send failed'
		sys.exit()
	 
	print 'Message send successfully'


	#Now receive data
	reply = s.recv(512)
	 
	print reply
	
	t1temp=t1temp1*10000+t1temp2*100+t1temp3


	#Send some data to remote server
	message = "{\"method\": \"upload\",\"data\":[{\"Name\":\""+sensor1+"\",\"Value\":\""+repr(t1temp)+"\"},{\"Name\":\""+sensor2+"\",\"Value\":\""+repr(t2temp)+"\"},{\"Name\":\""+sensor3+"\",\"Value\":\""+repr(t3temp)+"\"}]}&^!"
	 
	try :
		#Set the whole string
		s.sendall(message)
	except socket.error:
		#Send failed
		print 'Send failed'
		sys.exit()
		
	print 'Message send successfully'


	#Now receive data
	reply = s.recv(512)
	 
	print reply
	time.sleep(5)
	


