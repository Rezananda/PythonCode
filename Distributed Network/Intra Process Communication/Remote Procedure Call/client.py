#Import xmlrpc client
import xmlrpc.client

# Koneksikan ke server RPC
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:7778/")

# Panggil fungsinya

#Penjumlahan
hasil = proxy.penjumlahan(20, 10)
print("20+10 :",hasil)

#Pengurangan
hasil = proxy.pengurangan(20, 10)
print("20-10 :",hasil)

#Perkalian
hasil = proxy.perkalian(20, 10)
print("20x10 :",hasil)

#Pembagian
hasil = proxy.pembagian(20, 10)
print("20/10 :",hasil)

#Prima
hasil = proxy.prima(17)
print("17 adalah Prima :",hasil)