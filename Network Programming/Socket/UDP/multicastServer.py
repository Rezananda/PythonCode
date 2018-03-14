import time
import struct
import socket
import datetime

Port = 8123
Group = '127.0.0.1'
TTL = 1
now = datetime.datetime.now()

def sender(group):
    addrinfo = socket.getaddrinfo(group, None)[0]

    s = socket.socket(addrinfo[0], socket.SOCK_DGRAM)

    ttl_bin = struct.pack('@i', TTL)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl_bin)

    while True:
        data=now.strftime("%A %d. %B %Y").encode('ascii')
        s.sendto(data, (addrinfo[4][0], Port))
        time.sleep(1)

sender(Group)