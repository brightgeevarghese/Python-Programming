import socket

# create a socket object
s = socket.socket()  # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Associate socket object with a port number (0 to 65535)
# to reserve a port number for our service
s.bind(('127.0.0.1', 2500))
# keep our system in listening mode
s.listen()
while True:
    # wait for connection request
    mySocket, addressOfOtherSystem = s.accept()
    print('Connection accepted from '+str(addressOfOtherSystem))
    # receive data from system-2
    msg = mySocket.recv(100)
    print(msg.decode('utf-8'))
    # send welcome msg to system-2
    mySocket.send(bytes('welcome', 'utf-8'))
    # close mySocket
    mySocket.close()
