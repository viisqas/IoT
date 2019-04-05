import time
from IPython import embed
from math import sqrt
import json

import paho.mqtt.client as mqtt

results = []

# The callback for when the client receives a CONNACK response from the server.
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    results.append(json.lodas(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("159.69.95.154", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# ret= client.publish("house/bulb1","on")
client.loop_forever()

embed()
