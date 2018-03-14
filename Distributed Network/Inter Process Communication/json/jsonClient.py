import socket,random,json,time

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect( ("127.0.0.1", 6667) )

while True:
    temperature=random.randint(4,8)
    humidity=random.randint(30,88)
    oxygen=random.randint(50,75)

    data={'temperature':temperature,'humidity':humidity,'oxygen':oxygen}
    tcp_sock.sendall( (json.dumps(data)).encode('ascii') )

    time.sleep(1)
    
    data = tcp_sock.recv(1024)
    data = data.decode('ascii')
    print(data)

tcp_sock.close()