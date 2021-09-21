import dht
import machine
import time
import network
import urequests

from wifilib import conecta
print('Conectando a internet.')
station = conecta("TiraOZoio","NaoVaiRoubarAMinhaSenhaNão")
if not station.isconnected():
        print('Não conectado :(')
else:
    print('conectado!')
    print('Acessando o site ThingSpeak...')
    print('Coletando medidas.')
        
    d = dht.DHT11(machine.Pin(4))
    d.measure()
    temperatura = d.temperature()
    humidade = d.humidity()
    
    print('Medidas coletadas')
    print('Temp:'+ str(temperatura))
    print('Hum:'+ str(humidade))
    
    tempRes = 'https://api.thingspeak.com/update?api_key=H6R785VG8C1TYHIZ&field1='+ str(temperatura)
    res = urequests.get(tempRes)
    print(res.text)
    
    humRes = 'https://api.thingspeak.com/update?api_key=H6R785VG8C1TYHIZ&field2='+ str(humidade)
    time.sleep(20)
    res2 = urequests.get(humRes)
    print(res2.text)
    
    print('Processo finalizado!')