# Ahmad Riyadh Al Faathin - www.faathin.com - https://github.com/riyadh11
# Chat Client menggunakan Select
import socket, select, string, sys, json
 
def prompt() :
    print("<Kamu> ", end="")
    sys.stdout.flush()
 
#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 4) :
        print ("Usage : python3 client.py hostname port username")
        sys.exit()
     
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    USERNAME = sys.argv[3]
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # Menghubungkan ke server chat
    try :
        s.connect((HOST, PORT))
        USERNAME="[LOGIN]"+USERNAME
        s.send(USERNAME.encode("ascii"))
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
                        if(data["flag"]=="Private"):
                            print("\r<"+data["sender"]+":private>"+data["message"], end="")
                        else:
                            print("\r<"+data["sender"]+">"+data["message"], end="")
                        prompt()
                
                #User memasukkan pesan
                else :
                    msg = sys.stdin.readline()
                    s.send(msg.encode("ascii"))
                    prompt()
        except KeyboardInterrupt:
            print("BYE")
            s.send("[LOGOUT]".encode('ascii'))
            sys.exit()

                
