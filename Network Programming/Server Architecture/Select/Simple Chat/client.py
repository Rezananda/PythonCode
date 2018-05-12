# Ahmad Riyadh Al Faathin - www.faathin.com - https://github.com/riyadh11
# Chat Client menggunakan Select
import socket, select, string, sys, json, datetime

def prompt() :
    print("<Kamu> ", end="")
    sys.stdout.flush()

#Fungsi untuk mengirimkan pesan
def send(sock,message,flag) :
    payload=createMessage(message,flag)
    sock.send(json.dumps(payload).encode("ascii"))

#Fungsi untuk membuat pesan json
def createMessage(message,flag) :
    return {
        "username":USERNAME,
        "message":message.strip(),
        "flag":flag,
        "time":now.strftime("%A %d. %B %Y")
        }

#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 4) :
        print ("Usage : python3 client.py hostname port username")
        sys.exit()
        
    now = datetime.datetime.now()
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    USERNAME = sys.argv[3]
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # Menghubungkan ke server chat
    try :
        s.connect((HOST, PORT))
        send(s,USERNAME,"login")
    except :
        print ("Cannot Connect to Server")
        sys.exit()
    
    prompt()
     
    while 1:
        try:
            socket_list = [sys.stdin, s]
            
            # Mencoba mendapatkan daftar socket yang readable
            read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
            
            for sock in read_sockets:
                #Ada pesan masuk dari server
                if sock == s:
                    data = sock.recv(4096)
                    if not data :
                        print ("\nCannot Connect to Server")
                        sys.exit()
                    else :
                        #print data
                        data=json.loads(data.decode("ascii"))
                        print("\r<"+data["username"]+":"+data['flag']+"> "+data["message"]+"\n", end="")
                        prompt()
                
                #User memasukkan pesan
                else :
                    msg = sys.stdin.readline()
                    send(s,msg,"message")
                    prompt()
        except KeyboardInterrupt:
            print("BYE")
            send(s,USERNAME,"logout")
            sys.exit()