import socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.bind( ("0.0.0.0", 6667) )
tcp_sock.listen(100)

while True :
    conn, client_addr = tcp_sock.accept()
    data = conn.recv(100)
    data = data.decode('ascii')
    data = "OK "+data
    conn.send( data.encode('ascii') )
    conn.close()