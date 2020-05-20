# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime

#def on_publish(client, userdata, result):
#    print("Mengirimkan \n")

# definisikan nama broker yang akan digunakan
broker_address="localhost"

# buat client baru bernama P2
print("creating new instance")
client = mqtt.Client("P2") 
#client.on_publish=on_publish

# koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=3333) 

# mulai loop client
client.loop_start()

# lakukan 20x publish topik 1
print("publish something")
for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang topik 1
    client.publish("bulb1",str(datetime.datetime.now())+" => "+str(i))

#stop loop
client.loop_stop() 