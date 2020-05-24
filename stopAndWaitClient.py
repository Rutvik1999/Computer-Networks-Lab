import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('127.0.0.1', 11111))
print(soc.recv(1024).decode('utf-8'))
soc.send("ACK".encode('utf-8'))
while True:
    msg = soc.recv(1024)
    print("Message Received : " + msg.decode('utf-8'))
    soc.send("ACK".encode('utf-8'))
    if msg.decode('utf-8') == 'bye':
        break
    sen = input("Enter message to send : ")
    soc.send(sen.encode('utf-8'))
    if(soc.recv(24).decode('utf-8') == "ACK"):
        print("***ACK Recieved***")
    if sen == 'bye':
        break
soc.close()
