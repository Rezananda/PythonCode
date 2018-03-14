# Import library flask
from flask import Flask, request
import json

# Inisiasi app flask sebagai server
app = Flask("Hello App")

data_mahasiswa = [
    {
        "nim" : 123,
        "nama" : "Andi",
        "prodi" : "TIF"
    },
    {
        "nim" : 456,
        "nama" : "Budi",
        "prodi" : "TekKom"
    }
]

# Mendefinisikan fungsi yang akan menghandle method GET dengan URL '/'
@app.route('/mahasiswa', methods=['GET'])
# Kembalikan data seluruh mahasiswa
def handle_get():
    # Konversi dari list/dictionary ke string format JSON
    return json.dumps(data_mahasiswa)

# Fungsi untuk handle tambah data
@app.route('/mahasiswa', methods=['PUT'])
def tambah_mahasiswa():
    # Baca body request
    nim = request.json['nim']
    nama = request.json['nama']
    prodi = request.json['prodi']
    # Buat dictionary baru
    mahasiswa_baru = {
        'nama' : nama,
        'nim' : nim,
        'prodi': prodi
    }
    #Tambahkan ke list data mahasiswa
    data_mahasiswa.append(mahasiswa_baru)
    return "OK"

# Get satu mahasiswa
@app.route('/mahasiswa/<int:nim>', methods=['GET'])
def get_satu_mahasiswa(nim):
    for mahasiswa in data_mahasiswa:
        if(mahasiswa['nim']==nim):
            return json.dumps(mahasiswa)
    #Data tidak diubah
    return "Oops Not Found!"

# Fungsi untuk handle ubah data
@app.route('/mahasiswa/<int:nim>', methods=['PATCH'])
def ubah_mahasiswa(nim):
    # Baca body request
    nama = request.json['nama']
    prodi = request.json['prodi']
    # Cari berdasarkan nim
    
    for mahasiswa in data_mahasiswa:
        if(mahasiswa['nim']==nim):
            #Mengubah Data
            mahasiswa['nama']=nama
            mahasiswa['prodi']=prodi
            return "OK"
    #Data tidak diubah
    return "Oops Not Found!"

# Fungsi untuk handle hapus data
@app.route('/mahasiswa/<int:nim>', methods=['DELETE'])
def hapus_mahasiswa(nim):
    # Cari berdasarkan nim
    for mahasiswa in data_mahasiswa:
        if(mahasiswa['nim']==nim):
            #Menghapus Data
            data_mahasiswa.remove(mahasiswa)
            return "OK"
    #Data tidak dihapus
    return "Oops Not Found!"


# Jalankan server Flask
app.run(port=7777)