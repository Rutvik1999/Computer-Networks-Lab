import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input("Ener message to send : ")
s.sendto(data.encode('utf-8'), ("127.0.0.1", 11112))
while True:
    data, addr = s.recvfrom(1024)
    print("Message Received : " + data.decode('utf-8'))
    if data.decode('utf-8') == 'bye':
        break
    sen = input("Enter message to send : ")
    s.sendto(sen.encode('utf-8'),("127.0.0.1",11112))
    if sen == 'bye':
        break
s.close()
