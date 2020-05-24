import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 11112))
while True:
    msg = s.recv(1024)
    print("Message Received : " + msg.decode('utf-8'))
    if msg.decode('utf-8') == 'bye':
        break
    sen = input("Enter message to send : ")
    s.send(sen.encode('utf-8'))
    if sen == 'bye':
        break
s.close()
