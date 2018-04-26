# Ahmad Riyadh Al Faathin - www.faathin.com - https://github.com/riyadh11
# Chat server menggunakan Select
 
import socket, select, string, sys, json
 
#Fungsi untuk mengirimkan pesan broadcast
def broadcast_data (sock, message):
    #Tidak mengirimkan pesan ke pengirim awal dan socket bind
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(json.dumps(message).encode("ascii"))
            except :
                # client tidak dapat dikirimi pesan
                socket.close()
                CONNECTION_LIST.remove(socket)

def get_name (sock):
    for client in CLIENT_LIST :
        if(sock==client[0]) :
            return client[1]
    return False

def check_user (username):
    for client in CLIENT_LIST :
        if(client[1]==username):
            return client
    return False

def private_data (username,message):
    socket=check_user(username)
    if(socket==False):
            return False
    else:
        socket=socket[0]
        try :
            socket.send(json.dumps(message).encode("ascii"))
            return True
        except :
            # client tidak dapat dikirimi pesan
            socket.close()
            CONNECTION_LIST.remove(socket)
            return False

def someone_logout(sock):
    data={
        "sender": "Server",
        "message": "%s Left the Room\n" % get_name(sock),
        "flag": "Broadcast"
        }
                    
    broadcast_data(sock, data)
    sock.close()
    CONNECTION_LIST.remove(sock)
    CLIENT_LIST.remove([sock,get_name(sock)])
 
if __name__ == "__main__":
    # Argument Port
    if(len(sys.argv) < 3) :
        print ("Usage : python3 server.py hostname port")
        sys.exit()

    # List socket dari client
    CONNECTION_LIST = []
    CLIENT_LIST = []
    RECV_BUFFER = 4096
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # Tambahkan setiap client ke daftar socket
    CONNECTION_LIST.append(server_socket)
 
    print ("[Info]Chat Server running at interface %s port %s" % (str(HOST),str(PORT)) )
 
    try:
        while 1:
            # Mendapatkan client aktif
            read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
    
            for sock in read_sockets:
                #Ada Client baru
                if sock == server_socket:
                    # Mengatur client baru
                    sockfd, addr = server_socket.accept()
                    CONNECTION_LIST.append(sockfd)
                    print ("[Info]Client (%s, %s) Connected" % addr)
                
                #Terdapat pesan masuk dari client
                else:
                    # Memproses data dari client
                    try:
                        data = sock.recv(RECV_BUFFER)
                        if data:
                            Message=data.decode("ascii")
                            if "[LOGIN]" in Message :
                                clientName=Message[7::]
                                print("[Info]Login "+clientName)
                                User=check_user(Message[7::])
                                if(User==False):
                                    print("[Info]Success Login "+clientName)
                                    data={
                                        "sender": "Server",
                                        "message": "Selamat Bergabung di Group Chat\n",
                                        "flag": "Anouncement"
                                        }

                                    sockfd.send((json.dumps(data)).encode("ascii"))

                                    data={
                                        "sender": "Server",
                                        "message": "%s Join the Room\n" % clientName,
                                        "flag": "Anouncement"
                                        }
                                    broadcast_data(sockfd, data)

                                    data=[sockfd,Message[7:]]
                                    CLIENT_LIST.append(data)
                                else:
                                    print("[Warn]Error Login "+clientName)
                                    data={
                                        "sender": "Server",
                                        "message": "Username sudah digunakan, Log Out!\n",
                                        "flag": "Anouncement"
                                        }

                                    sockfd.send((json.dumps(data)).encode("ascii"))
                                    sockfd.close()
                                    CONNECTION_LIST.remove(sockfd)
                                    CLIENT_LIST.remove([sockfd,get_name(sockfd)])
                            elif "[LOGOUT]" in Message :
                                print("[Info]Log Out ")
                                someone_logout(sockfd)
                            elif "\pc " in Message:
                                print("[Info]Private Message")
                                clientName=get_name(sock)
                                personal=Message[4:].split(" ")[0]
                                Message=Message[len(personal)+5:]
                                data={
                                    "sender": clientName,
                                    "message": Message,
                                    "flag": "Private"
                                    }
                                if private_data(personal,data)==False:
                                    print("[Warn]Cannot Send Private Message to  "+clientName)
                                    data={
                                        "sender": "Server",
                                        "message": "Private Chat tidak bisa dikirimkan!",
                                        "flag": "Anouncement"
                                        }
                                    sockfd.send((json.dumps(data)).encode("ascii"))
                            elif "\list" in Message:
                                print("[LOG]Request List")
                                list=[]
                                for client in CLIENT_LIST :
                                    list.append(client[1])
                                data={
                                    "sender": "Server",
                                    "message": "List Member : "+str(list)+"\n",
                                    "flag": "Anouncement"
                                    }
                                sockfd.send((json.dumps(data)).encode("ascii"))
                            else :
                                print ("[Info]Broadcasting")
                                clientName=get_name(sock)
                                data={
                                    "sender": clientName,
                                    "message": data.decode("ascii"),
                                    "flag": "Broadcast"
                                    }
                                broadcast_data(sock, data)
                    except:
                        someone_logout(sock)
                        continue
    except KeyboardInterrupt:
        print("[LOG]Shutting Down")
        sys.exit()
    finally:
        server_socket.close()
