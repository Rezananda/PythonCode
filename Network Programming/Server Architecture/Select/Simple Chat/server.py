# Ahmad Riyadh Al Faathin - www.faathin.com - https://github.com/riyadh11
# Chat server menggunakan Select
 
import socket, select, string, sys, json, datetime

#Mengirimkan pesan
def send(sock,payload) :
    try :
        sock.send(json.dumps(payload).encode("ascii"))
        return True
    except :
        # client tidak dapat dikirimi pesan
        sock.close()
        CONNECTION_LIST.remove(socket)
        return False

#Fungsi untuk membuat pesan json
def createMessage(username,message,flag) :
    return {
        "username" : username,
        "message": message,
        "flag": flag,
        "time": now.strftime("%A %d. %B %Y")
        }

#Fungsi untuk mengirimkan pesan broadcast
def broadcastData (sender, receiver, message, flag):
    #Tidak mengirimkan pesan ke pengirim awal dan socket bind
    payload=createMessage(sender,message,flag)
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != receiver :
            send(socket,payload)
    return True

#Fungsi untuk mengirimkan pesan private message
def privateData (sender,receiver,message,flag):
    socket=checkUser(receiver)
    if(socket==False):
            return False
    else:
        socket=socket[0]
        payload=createMessage(sender,message,flag)
        return send(socket,payload)

#Fungsi untuk mendapatkan sock dari username
def getName (sock):
    for client in CLIENT_LIST :
        if(sock==client[0]) :
            return client[1]
    return False

#Fungsi untuk mendapatkan data dari sebuah sock
def checkUser (username):
    for client in CLIENT_LIST :
        if(client[1]==username):
            return client
    return False

#Fungsi untuk mengirimkan pesan broadcast logout
def someoneLogOut(sock):
    broadcastData("Server", sock ,"%s Left the Room" % getName(sock), "Anouncement")
    sock.close()
    CONNECTION_LIST.remove(sock)
    CLIENT_LIST.remove([sock,getName(sock)])
 
if __name__ == "__main__":
    # Argument Port
    if(len(sys.argv) < 3) :
        print ("Usage : python3 server.py hostname port")
        sys.exit()
    #Date
    now = datetime.datetime.now()

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
                            data=json.loads(data.decode("ascii"))
                            if(data["flag"]=="login"):
                                sender=data['message']
                                print("[Info]Login "+sender)
                                User=checkUser(sender)
                                if(User==False):
                                    print("[Info]Success Login "+sender)
                                    CLIENT_LIST.append([sock,sender])
                                    privateData("Server",sender,"Selamat Bergabung di Group Chat","login")
                                    broadcastData("Server",sock,"%s Join the Room" % sender, "Anouncement")
                                else:
                                    print("[Warn]Error Login "+sender)
                                    send(sock,createMessage("Server","Username sudah digunakan, Log Out!","login"))
                                    sock.close()
                                    CONNECTION_LIST.remove(sock)
                            elif(data['flag']=="logout"):
                                print("[Info]Log Out ")
                                someoneLogOut(sock)
                            else:
                                message=data['message']
                                if("\pc " in message):
                                    #Mencoba mengirim PC
                                    print("[Info]Private Message")
                                    sender=data['username']
                                    receiver=message[4:].split(" ")[0]
                                    message=message[len(receiver)+5:]
                                    #Jika PC gagal dikirim
                                    if privateData(sender,receiver,message,"private")==False:
                                        print("[Warn]Cannot Send Private Message to "+receiver)
                                        privateData("Server",sender,"Private Chat tidak bisa dikirimkan","feature")
                                elif("\list" == message):
                                    print("[LOG]Request List")
                                    list=[]
                                    for client in CLIENT_LIST :
                                        list.append(client[1])
                                    privateData("Server",data['username'],"List Member : "+str(list),"feature")
                                else:
                                    print ("[Info]Broadcasting")
                                    broadcastData(data['username'],sock,data['message'],"broadcast")
                    except:
                        someoneLogOut(sock)
                        continue
    except KeyboardInterrupt:
        print("[LOG]Shutting Down")
        sys.exit()
    finally:
        server_socket.close()