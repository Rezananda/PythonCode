### Ahmad Riyadh Al Faathin - 155150207111052 - SKT C - Faathin.com ###
import socket,threading,signal,sys

def handle_thread(conn):
    while True :
        try :
            data = conn.recv(1024)
            data = data.decode('ascii')
            
            print('Receive data :'+data)
            
            data = "[ACK] "+data
            conn.send( data.encode('ascii') )
        except (socket.error) :
            conn.close()
            print("Connection Closed by Peer")
            break
        except :
            print ("Unexpected error:", sys.exc_info()[0])
            conn.close()
            break


tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.bind( ("0.0.0.0", 6667) )
tcp_sock.listen(1024)

print('Listening at', tcp_sock.getsockname())
print("Press Crtl+c to exit...")
while True :
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        conn, client_addr = tcp_sock.accept()
        t = threading.Thread(target=handle_thread, args=(conn,))
        t.start()
    except KeyboardInterrupt:
        break