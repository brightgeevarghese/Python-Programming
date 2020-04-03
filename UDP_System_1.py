import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind socket with a port number - 2000
s.bind(('127.0.0.1', 2000))
while True:
    print('Ready to receive ')
    # code to receive data
    data, addressInfo = s.recvfrom(100)
    print(data.decode('utf-8') + ' from ' + str(addressInfo))
    print('Ready to send ')
    # code to send data
    s.sendto(bytes(input(), 'utf-8'), ('127.0.0.1', 3000))
