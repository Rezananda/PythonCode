# Ahmad Riyadh Al Faathin - www.faathin.com - https://github.com/riyadh11
# Import library http client
import http.client

ip_server = "127.0.0.1"
port_server = 7777

# Inisiasi koneksi ke server
conn = http.client.HTTPConnection(ip_server, port=port_server)

def perangkat(device,status):    
    # Kirim request POST /home
    conn.request('POST', '/home/'+device+'/'+status)
    # Dapatkan responsenya
    resp = conn.getresponse().read()
    print(resp)

perangkat("Lampu","1")
# perangkat("Lampu","0")
# perangkat("Kulkas","1")
# perangkat("Kulkas","0")
# perangkat("Kipas Angin","1")
# perangkat("Kipas Angin","0")

