# Ahmad Riyadh Al Faathin - www.faathin.com - https://github.com/riyadh11
# Import library mqtt, Flask
import paho.mqtt.client as mqtt_client
from flask import Flask, request

# Inisiasi app flask sebagai server
app = Flask("Middleware Broker Rest + MQTT")

# Inisiasi client sebagai publisher
pub = mqtt_client.Client()

# Fungsi untuk handle tambah data
@app.route('/home/<string:device>/<string:status>', methods=['POST'])
def getClient(device,status):
    if(status=="1"):
        message="Nyala"
    elif(status=="0"):
        message="Mati"
    else:
        return "Status tidak didukung"
    
    if(status=="1" or status=="0"):
        if(device=="Lampu" or device=="Kipas Angin" or device=="Kulkas"):
            # Publish message
            pub.publish("/"+device, message)
            return "Perangkat "+device+" Diubah ke mode "+message
        else :
            return "Perangkat '"+device+"' Tidak Didukung!"
    
# Koneksikan ke broker
pub.connect("127.0.0.1", 1883)
# Jalankan server Flask
app.run(port=7777)