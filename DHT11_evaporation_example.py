import board
import adafruit_dht
import time

# Initialize DHT11 sensor
dht11 = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temperature_c = dht11.temperature
        humidity = dht11.humidity
        temperature_f = temperature_c * 9 / 5 + 32
        print(f"Temperature: {temperature_c}C / {temperature_f}F, Humidity: {humidity}%")
    except RuntimeError as e:
        print(f"Error reading DHT11: {e}")
    time.sleep(2)
