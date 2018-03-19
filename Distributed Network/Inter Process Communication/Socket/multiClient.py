import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect( ("127.0.0.1", 6667) )

for i in range(0,2):
    data = "Hello World"
    tcp_sock.send( data.encode('ascii') )

    data = tcp_sock.recv(100)
    data = data.decode('ascii')
    print(data)

tcp_sock.close()