import paho.mqtt.client as mqtt
import requests
import json

MQTT_HOST = '10.21.160.16'
MQTT_PORT = 1883
MQTT_TOPIC = 'campinas/temperatura'

API_KEY = '3ab0fa205b9719a115400000ac5504b7'
CITY = 'campinas'
UNITS = 'metric'


def on_connect(client, userdata, flags, rc):
    print('Conectado ao broker MQTT com sucesso.')
    client.subscribe(MQTT_TOPIC)


def on_publish(client, userdata, mid):
    print(f'Mensagem publicada no tópico {MQTT_TOPIC}, com a seguinte mensagem: {mid.payload.decode()}')


client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(MQTT_HOST, MQTT_PORT, 60)

url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units={UNITS}&appid={API_KEY}'
response = requests.get(url)
data = json.loads(response.text)
temperatura = data['main']['temp']
mqtt.single(MQTT_TOPIC, temperatura, MQTT_HOST)
client.publish(MQTT_TOPIC, temperatura)

client.disconnect()
