import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 11111
s.bind(("", port))
s.listen(5)
c, addr = s.accept()
print("Got Connection from : " + str(addr))
c.send("Connected to Server".encode('utf-8'))
if(c.recv(24).decode('utf-8') == "ACK"):
		print("---ACK Recieved---")
while True:	
	sen = input("Enter Message to Send : ")
	c.send(sen.encode('utf-8'))
	if sen == "bye":
		break
	if c.recv(24).decode('utf-8') == "ACK" :
		print("***ACK Recieved***")
	msg = c.recv(1024)
	print("Received : " + msg.decode('utf-8'))
	c.send("ACK".encode('utf-8'))
	if msg == 'bye':
		break
c.close()
s.close()
