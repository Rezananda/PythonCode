### Ahmad Riyadh Al Faathin - 155150207111052 - SKT C - Faathin.com ###
# Import library mqtt, random, json, time
import socket,threading,signal,sys, struct,json, datetime, os, errno

def handle_thread(conn):
    while True :
        try :
            data=recv_msg(conn)
            if(data!=None):
                data=data.decode('utf-8')
                print("[Receive Data]")
                niceJson = json.loads(data)

                directory = datetime.datetime.now().strftime("%d%m%y")
                fileName = datetime.datetime.now().strftime("%H%M") + ".json"

                # Folder Belum Ada
                if (os.path.isdir(directory) == False):
                    try:
                        os.makedirs(directory)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise

                with open(directory + "/" + fileName, 'w') as outfile:
                    json.dump(niceJson, outfile, sort_keys=False, indent=4,
                              ensure_ascii=False)
        except (socket.error) :
            conn.close()
            print("[Warn] Connection Closed by Peer")
            break
        except :
            print ("[Warn] Unexpected error:", sys.exc_info())
            conn.close()
            break

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

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.bind( ("0.0.0.0", 5555) )
tcp_sock.listen(1024)

print('[Info] Listening at', tcp_sock.getsockname())
print("[Info] Press Crtl+c to exit...")
while True :
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        conn, client_addr = tcp_sock.accept()
        t = threading.Thread(target=handle_thread, args=(conn,))
        t.start()
    except KeyboardInterrupt:
        break