import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 11112

s.bind(("", port))

s.listen(1)
while True:
    c, addr = s.accept()
    print("Got Connection from = " + str(addr))

    while True:
        sen = input("Enter Message to Send = ")
        c.send(sen.encode('utf-8'))
        if sen == "bye":
            break
        msg = c.recv(1024)
        print("Received = " + msg.decode('utf-8'))
        if msg == 'bye':
            break
    c.close()
    des = input("Do you want to continue? (y or n) : ")
    if des == 'n':
        break
s.close()
