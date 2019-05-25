from random import randint
from time import sleep
from Graficarpersones import grafica

 

def distancia():
    persones1 = randint(0,1)
    return persones1

llistapersones=[]
minuts=0

while minuts<10:
    persones = 0
    for segons in range(10):
        persones2 = distancia()
        if persones2 == 1:
            persones += 1
        sleep(1)
    llistapersones.append(persones)
    minuts += 1
grafica(llistapersones)
    







