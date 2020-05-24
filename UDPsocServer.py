import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 11112
s.bind(("", port))

data, addr = s.recvfrom(1024)
print("Got Connection from = " + str(addr))
print("Received = " + data.decode('utf-8'))
while True:
    sen = input("Enter Message to Send = ")
    s.sendto(sen.encode('utf-8'),addr)
    if sen == "bye":
        break
    data, addr = s.recvfrom(1024)
    print("Received = " + data.decode('utf-8'))
    if data.decode('utf-8') == 'bye':
        break
s.close()
