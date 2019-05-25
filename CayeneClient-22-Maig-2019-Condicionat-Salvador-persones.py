import cayenne.client
from random import randint
from time import sleep



def cayene(persones):
    client.virtualWrite(1,persones)
    

    

def distancia():
    persones1 = randint(0,1)
    return persones1
  

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME = "cabb3650-7c77-11e9-beb3-736c9e4bf7d0"
MQTT_PASSWORD = "0abe0b568fd0ba4a0648c59c7d5a3a71ec534e7d"
MQTT_CLIENT_ID = "5ff91f30-7f1a-11e9-b4eb-6bf2c2412b24"
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)


while True:
    client.loop()
    persones = 0
    for segons in range(10):
        persones2 = distancia()
        if persones2 == 1:
            persones += 1
        sleep(1)
    cayene(persones)
    







