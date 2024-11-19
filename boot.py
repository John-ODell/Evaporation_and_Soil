import time
import board
import analogio
import adafruit_dht
import busio
import digitalio
import adafruit_sdcard
import storage

soil_moisture = analogio.AnalogIn(board.VN) 
water_level = analogio.AnalogIn(board.VP)  
dht11 = adafruit_dht.DHT11(board.D4)

DRY_VALUE = 68.0  # Dry soil reading
WET_VALUE = 29.0  # Wet soil reading

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.D5) 
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

def get_calibrated_soil_moisture():
    raw_value = (soil_moisture.value / 65535) * 100
    calibrated_value = (raw_value - DRY_VALUE) / (WET_VALUE - DRY_VALUE) * 100
    return max(0, min(100, calibrated_value))

def get_water_level():
    return (water_level.value / 65535) * 100 

def read_dht11():
    try:
        temperature_c = dht11.temperature
        humidity = dht11.humidity
        temperature_f = temperature_c * 9 / 5 + 32
        return temperature_c, temperature_f, humidity
    except RuntimeError as error:
        print(error.args[0])
        return None, None, None

def save_to_csv(data):
    with open("/sd/sensor_data.csv", "a") as file:
        file.write(",".join(map(str, data)) + "\n")

# Main loop
while True:
    timestamp = time.time()
    soil_value = get_calibrated_soil_moisture()
    water_value = get_water_level()
    temperature_c, temperature_f, humidity = read_dht11()

    print(timestamp)
    print(f"Soil Moisture: {soil_value:.2f}%")
    print(f"Water Level: {water_value:.2f}%")
    print(f"Temperature: {temperature_c}C")
    print(f"Temperature: {temperature_f}F")
    print(f"Humidity: {humidity}%")

    if temperature_c is not None:
        data = [timestamp, soil_value, water_value, temperature_c, temperature_f, humidity]
        save_to_csv(data)
        print(f"Data logged at {timestamp}: Soil: {soil_value:.2f}%, Water: {water_value:.2f}, Temp: {temperature_c}C, {temperature_f}F, Humidity: {humidity}%")    
    save_to_csv(data)

    # Wait for 1 hour
    time.sleep(3600)
