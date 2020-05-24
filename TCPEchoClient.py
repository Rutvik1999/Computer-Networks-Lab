import socket
# Python 2.7
soc = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
msg_send = raw_input("Enter a message to send: ")
soc.connect(("127.0.0.1", 5555))
soc.send(msg_send)
print("Message from Server : " + str(soc.recv(1024)))
soc.close()
