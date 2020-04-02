import socket

# create socket object
s = socket.socket()   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to a port number
# s.bind(('127.0.0.1', 3000))
# send a connection request to system-1
s.connect(('127.0.0.1', 2500))
# send data to system - 1
s.send(bytes('from system-1 : Good day', 'utf-8'))
# receive the data
msg = s.recv(100)
# decode the msg and print it
print(msg.decode('utf-8'))
# close the socket
s.close()

