import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('',5555))
soc.listen(5)
while True :
	c, addr = soc.accept()
	recv_data = c.recv(1024)
	print("Received" + recv_data)
	print("Echoing it back\n")
	c.send(recv_data)
	c.close()
	