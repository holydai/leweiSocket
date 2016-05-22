#handling errors in python socket programs
 
import socket   #for sockets
import sys  #for exit
 
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
sensor='T1'
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip

#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip

value=raw_input("enter a number:")

while  value:

	#Send some data to remote server
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


	#Send some data to remote server
	message = "{\"method\": \"upload\",\"data\":[{\"Name\":\""+sensor+"\",\"Value\":\""+value+"\"}]}&^!"
	 
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
	value=raw_input("enter a number:")
