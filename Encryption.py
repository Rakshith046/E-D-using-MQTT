from random import randint, seed

import paho.mqtt.client as paho
import sys

message= input("Enter the text:")
variable = ""
hexa_= ""

S = int(input("Set the seed:"))
seed(S)
for i in message:
    key= randint(1,10)
    asc_val= ord(i)
    xor_= asc_val ^ key
    encrypted =chr(xor_)
    variable += encrypted
for i in variable:
     hexa = hex(ord(i))
     hexa_ += hexa[2:].zfill(2)
print("After encrypting:",hexa_) 

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("cloud not connect to MQTT broker")
    sys.exit(-1)

client.publish("encrypt",hexa_, 0)

client.disconnect()
