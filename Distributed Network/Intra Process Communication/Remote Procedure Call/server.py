# Import library xmlrpc server
import xmlrpc.server

# Inisiasi servernya
server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )

# Definisikan procedure/fungsi yang akan dipanggil dari client
def penjumlahan(a,b):
    return (a+b)

def pengurangan(a,b):
    return (a-b)

def perkalian(a,b):
    return (a*b)

def pembagian(a,b):
    return (a/b)

def prima(a):
    if a > 1:
        for i in range(2,a):
            if (a % i) == 0:
                return False
        else:
            return True
    else:
        return False

# Daftarkan fungsi yang akan dipanggil dari client
server.register_function(penjumlahan, 'penjumlahan')
server.register_function(pengurangan, 'pengurangan')
server.register_function(perkalian, 'perkalian')
server.register_function(pembagian, 'pembagian')
server.register_function(prima, 'prima')

# Jalankan service servernya
server.serve_forever()