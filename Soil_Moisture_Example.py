import board
import analogio
import time

# Initialize analog input for soil moisture sensor
soil_moisture = analogio.AnalogIn(board.VN)  

def get_soil_moisture():
   
    return (soil_moisture.value / 65535) * 100 

while True:
    soil_value = get_soil_moisture()
    print(f"Soil Moisture: {soil_value:.2f}%")
    time.sleep(1)
