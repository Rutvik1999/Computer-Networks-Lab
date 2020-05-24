import socket
soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soc.bind(('',5555))
print("UDP server up and listening")
while True :
	message = soc.recvfrom(1024)
	print("Received message from client: "+str(message))
	print("Echoing it back")
	soc.sendto(message[0], message[1])  # (clientMessage,clientAddress)
soc.close()
