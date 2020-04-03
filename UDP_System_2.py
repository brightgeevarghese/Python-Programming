import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind socket with a port number - 3000
s.bind(('127.0.0.1', 3000))
while True:
    print('Ready to send data ')
    # code to send data
    s.sendto(
        bytes(input(), 'utf-8'), # data to be sent
        ('127.0.0.1', 2000) # details of destination
    )
    # code to receive data
    print('Ready to receive')
    # data => received data
    # addressInfo => details of sender
    data, addressInfo = s.recvfrom(100)
    print(data.decode('utf-8') + ' from ' + str(addressInfo))
