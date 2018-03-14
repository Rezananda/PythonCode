import sys
import socket
import signal

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(srv_sockaddr)
print("Press Crtl+c to exit...")

while True:
    try:
        payload, cln_sockaddr = sock.recvfrom(16)
        msg = payload.decode('ascii')
        print('Receive "{}" from {}'.format(msg, cln_sockaddr))
    except KeyboardInterrupt:
        break