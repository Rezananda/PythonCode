#!/usr/bin/env python

import struct
import socket
from sys import argv

Port = 8123
Group = '225.0.0.250'
MYTTL = 1

def receiver(group):
    addrinfo = socket.getaddrinfo(group, None)[0]

    s = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(('', Port))

    group_bin = socket.inet_pton(addrinfo[0], addrinfo[4][0])

    mreq = group_bin + struct.pack('=I', socket.INADDR_ANY)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        data = s.recvfrom(1500)
        print(data[0].decode('ascii'))


receiver(Group)