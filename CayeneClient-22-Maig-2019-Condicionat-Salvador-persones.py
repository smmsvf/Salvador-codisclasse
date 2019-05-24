import cayenne.client
from random import randint
from time import sleep



def cayene(persones):
    client.virtualWrite(1,persones)
    

    

def distancia():
    persones1 = randint(0,1)
    return persones1
  

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME = "2dd7a530-d092-11e8-a056-c5cffe7f75f9"
MQTT_PASSWORD = "6d63b6a30a53c35a4abd3bc1b1876c470738a485"
MQTT_CLIENT_ID = "00035950-7c78-11e9-be3b-372b0d2759ae"
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)


while True:
    client.loop()
    persones = 0
    for segons in range(60):
        persones2 = distancia()
        if persones2 == 1:
            persones += 1
        sleep(1)
    cayene(persones)
    







