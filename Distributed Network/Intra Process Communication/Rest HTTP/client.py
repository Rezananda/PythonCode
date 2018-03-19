# Import library http client
import http.client
import json

ip_server = "127.0.0.1"
port_server = 7777

 # Kirim request GET dengan URL "/mahasiswa"
# Inisiasi koneksi ke server
conn = http.client.HTTPConnection(ip_server, port=port_server)

def get_mahasiswa():   
    # Kirim request ke server
    conn.request('GET', '/mahasiswa')
    # Baca response nya
    response = conn.getresponse().read()
    print( response.decode('ascii') )

def tambah_mahasiswa():    
    # Definisikan headernya
    headers = {"Content-type": "application/json"}
    # Definisikan bodynya
    mahasiswa_baru = {"nim": 210, "nama": "Joni", "prodi":"Sistem Komputer"}
    # Kirim request POST /mahasiswa
    conn.request('PUT', '/mahasiswa', json.dumps(mahasiswa_baru), headers)
    # Dapatkan responsenya
    resp = conn.getresponse().read()
    print(resp)

def ubah_mahasiswa():    
    # Definisikan headernya
    headers = {"Content-type": "application/json"}
    # Definisikan bodynya
    mahasiswa_baru = {"nama": "Johan","prodi":"Teknik Informatika"}
    # Kirim request PUT /mahasiswa
    conn.request('PATCH', '/mahasiswa/210', json.dumps(mahasiswa_baru), headers)
    # Dapatkan responsenya
    resp = conn.getresponse().read()
    print(resp)

def get_satu_mahasiswa():   
    # Kirim request ke server
    conn.request('GET', '/mahasiswa/210')
    # Baca response nya
    response = conn.getresponse().read()
    print( response.decode('ascii') )

def hapus_mahasiswa():   
    # Kirim request ke server
    conn.request('DELETE', '/mahasiswa/123')
    # Baca response nya
    response = conn.getresponse().read()
    print( response.decode('ascii') )

#tambah_mahasiswa()
get_mahasiswa()
#ubah_mahasiswa()
#get_satu_mahasiswa()
#hapus_mahasiswa()