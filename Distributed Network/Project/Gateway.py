### Ahmad Riyadh Al Faathin - 155150207111052 - SKT C - Faathin.com ###
# Import library paho mqtt
import paho.mqtt.client as mqtt_client
import socket, json, struct
from sys import argv, exit

# Fungsi untuk handle message yang masuk
def handle_message(mqttc, obj, msg):
    # Dapatkan topik dan payloadnya
    topic = msg.topic
    payload = msg.payload
    payload = payload.decode('utf-8')
    collect_data(payload)

# Fungsi menyimpan data
def collect_data(payload):
    if(len(data)<MAX_MESSAGE):
        data.append(json.loads(payload))
    else:
        send_msg(json.dumps(data).encode('utf-8'))
        data[:] = []
        print("[LOG] Sending Data")

# Fungsi mengirim data
def send_msg(msg):
    msg = struct.pack('>I', len(msg)) + msg
    # Koneksi ke Receiver
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.connect(("127.0.0.1", 5555))
    tcp_sock.send(msg)
    tcp_sock.close()

#main function
if __name__ == "__main__":
     
    if(len(argv) < 2) :
        print ("Usage : python3 Gateway.py <Number of Nodes>")
        exit()

    # Inisiasi client mqtt sebagai subscriber
    sub = mqtt_client.Client()

    # Koneksikan ke broker
    sub.connect("192.168.10.11", 1883)

    # List
    data = []

    # Define Buffer Time
    MINUTE = 1

    # Define Nodes
    NODES = int(argv[1])

    # Define Max Message
    MAX_MESSAGE = (MINUTE * 60 * NODES) + NODES

    # Daftarkan fungsinya untuk event on_message
    sub.on_message = handle_message

    # Subscribe ke sebuah topik
    sub.subscribe("/sensor/#")

    print('[Info] Subscribe at sensor')

    # Loop forever
    sub.loop_forever()