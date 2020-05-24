import select 
import sys
import socket

udpSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM);
ipAddress=''
port=12345

udpSocket.bind(("",port))
print "UDP server is up and running:"
clientID=[]
while True:
	inputStream_list=[sys.stdin,udpSocket]
	read_sockets,write_socket,error_socket=select.select(inputStream_list,[],[])	
	if udpSocket in read_sockets:
		message = udpSocket.recvfrom(1024)
		print "<recieved>" + str(message)
		clientID.append(message[1])
					
	if sys.stdin in read_sockets:
		for i in clientID:
			if not clientID:						
				print "No client in communication"	
			else:
				buf=raw_input()
				udpSocket.sendto(buf,i)
				print "<You>" + buf
		clientID=[]
