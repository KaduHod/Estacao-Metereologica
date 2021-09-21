import dht
import machine
import time

d = dht.DHT11(machine.Pin(4))
while True:
    d.measure()
    temperatura = d.temperature()
    humidade = d.humidity()
    if (temperatura > 31) and (humidade > 70):
        print("Temperatura de acordo com os requisitos necessários para ligar o relé")
        
    else:
        print("Temperatura não está acordo com os requisitos necessários para ligar o relé")
        
    print(humidade)
    print(temperatura)
    print("Temperatura: {} \n Humidade: {} \n\n ============= \n".format(d.temperature(), d.humidity()))
    time.sleep(5)