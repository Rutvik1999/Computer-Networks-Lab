import socket
# Python 2.7
soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg_send = raw_input("Enter a message to send: ")
soc.sendto(msg_send,("127.0.0.1",5555))
print("Message from server: " + str(soc.recvfrom(1024)))
soc.close()
