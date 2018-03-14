import sys
import socket
import signal
import datetime

now = datetime.datetime.now()
srv_port=sys.argv[1]
srv_sockaddr = ('', int(srv_port))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(srv_sockaddr)
print("Press Crtl+c to exit...")

while True:
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        payload, cln_sockaddr = sock.recvfrom(400)
        msg = payload.decode('ascii')
        print('Receive "{}" from {}'.format(msg, cln_sockaddr))
        if(msg=="Time?"):
            reply=now.strftime("%A %d. %B %Y").encode('ascii')
        elif(msg=="Date?"):
            reply = now.strftime("%H:%M:%S").encode('ascii')
        else:
            reply=("Don't understand what you're saying :"+msg).encode('ascii')

        sock.sendto(reply, cln_sockaddr)

    except KeyboardInterrupt:
        break