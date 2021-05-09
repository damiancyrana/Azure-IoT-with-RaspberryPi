import Adafruit_DHT
import time

DHT11_SENSOR = Adafruit_DHT.DHT11
DHT11_PIN = 4

while True:
    humidity, temp = Adafruit_DHT.read(DHT11_SENSOR, DHT11_PIN)
    if humidity is not None and temp is not None:
        print(f"Temp = {temp} C --- Humidity = {humidity} %")
    else:
        print("Connection to DHT11 sensor IS LOST!!!"); time.sleep(3)

