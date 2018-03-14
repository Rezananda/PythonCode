import socket
import threading

def handle_thread(conn):
    while True :
        try :
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "OK "+data
            conn.send( data.encode('ascii') )

        except (socket.error) :
            conn.close()
            print("Connection Closed by Peer")
            break

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.bind( ("0.0.0.0", 6667) )
tcp_sock.listen(1024)

while True :
    conn, client_addr = tcp_sock.accept()
    t = threading.Thread(target=handle_thread, args=(conn,))
    t.start()