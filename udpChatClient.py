import select 
import sys
import socket

udpSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM);
ipAddress=''
port=12345

while True:
	inputStream_list=[sys.stdin,udpSocket]
	read_sockets,write_socket,error_socket=select.select(inputStream_list,[],[])
	if udpSocket in read_sockets:
		message = udpSocket.recvfrom(1024)
		print "<recieved>" + str(message)
		if message[0]=="bye":
			udpSocket.close()
			break
	if sys.stdin in read_sockets:
		buf=raw_input()
		udpSocket.sendto(buf,(ipAddress,port))
		print "<You>" + buf
		if buf == "bye":
			udpSocket.close()
			break	
