import sys
import socket
srv_port = sys.argv[1]
msg = sys.argv[2]
srv_sockaddr, payload = ('<broadcast>',int(srv_port)), msg.encode('ascii')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
sock.sendto(payload, srv_sockaddr)


try:
    payload, cln_sockaddr = sock.recvfrom(400)
    msg = payload.decode('ascii')
    print('Receive "{}" from {}'.format(msg, cln_sockaddr))
except :
    print("Error!")