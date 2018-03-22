# Ahmad Riyadh Al Faathin - www.faathin.com - https://github.com/riyadh11
# Import library paho mqtt and sys
import paho.mqtt.client as mqtt_client
from sys import argv

device=argv[1]
if(device=="Lampu" or device=="Kipas Angin" or device=="Kulkas"):
    # Inisiasi client mqtt sebagai subscriber
    sub = mqtt_client.Client()
    # Koneksikan ke broker
    sub.connect("127.0.0.1", 1883)

    # Fungsi untuk handle message yang masuk
    def handle_message(mqttc, obj, msg):
        # Dapatkan topik dan payloadnya
        topic = msg.topic
        payload = msg.payload
        payload = payload.decode('ascii')
        # Print Status
        print(device +" Status : "+ payload)

    # Daftarkan fungsinya untuk event on_message
    sub.on_message = handle_message
    # Subscribe ke sebuah topik
    sub.subscribe("/"+device+"/#")
    # Print Daftar
    print("Perangkat didaftarkan sebagai "+device)

    # Loop forever
    sub.loop_forever()
else :
    print("Perangkat tidak didukung")