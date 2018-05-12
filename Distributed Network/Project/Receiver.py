### Ahmad Riyadh Al Faathin - 155150207111052 - SKT C - Faathin.com ###
# Import library mqtt, random, json, time
import socket,threading,signal,sys, struct,json, datetime, os, errno, select, signal
from StorageHandler import StorageHandler
from sys import argv

#main function
if __name__ == "__main__":
     
    if(len(argv) != 1) :
        print ("Usage : python3 Receiver.py")
        exit()
    
    Storage = StorageHandler("192.168.10.11",9000)

def handle_socket(conn):
    try :
        data=recv_msg(conn)
        if(data!=None):
            data=data.decode('utf-8')
            print("[Receive Data]")
            niceJson = json.loads(data)

            directory = "/Logs/"+datetime.datetime.now().strftime("%d%m%y")
            fileName = datetime.datetime.now().strftime("%H%M") + ".json"
            jsonData = json.dumps(niceJson, sort_keys=False,indent=4, separators=(',', ': '))
            
            Storage.write(directory+"/"+fileName, "w", jsonData)
                            
    except (socket.error) :
        conn.close()
        print("[Warn] Connection Closed by Peer")
    except :
        print ("[Warn] Unexpected error:", sys.exc_info())
        conn.close()

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setblocking(0)
serversock.bind(("0.0.0.0", 5555))
serversock.listen(1)
rlist = [serversock]

print('Listening at', serversock.getsockname())
print("Press Crtl+c to exit...")
while True:
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        readable, _, _ = select.select(rlist, [], [])
        for s in readable:
            if s is serversock:
                datasock, clientsockaddr = serversock.accept()
                datasock.setblocking(0)
                rlist.append(datasock)
                print('Client {} connected'.format(clientsockaddr))
            else:
                handle_socket(s)
    except KeyboardInterrupt:
        break

serversock.close()