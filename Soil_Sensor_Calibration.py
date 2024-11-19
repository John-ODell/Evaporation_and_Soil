import board
import analogio
import time

soil_moisture = analogio.AnalogIn(board.VN)  

# Calibrated dry and wet values
DRY_VALUE = 68.0  # Dry soil reading
WET_VALUE = 29.0  # Submerged in water reading

def get_calibrated_soil_moisture():
    raw_value = (soil_moisture.value / 65535) * 100
    calibrated_value = (raw_value - DRY_VALUE) / (WET_VALUE - DRY_VALUE) * 100
    return max(0, min(100, calibrated_value))

while True:
    soil_value = get_calibrated_soil_moisture()
    print(f"Soil Moisture: {soil_value:.2f}%")
    time.sleep(1)
    
# Use this code if you want to do more than one calibration
#def moving_average(values, new_value, size=10):
    #values.append(new_value)
    #if len(values) > size:
        #values.pop(0)
    #return sum(values) / len(values)

#history = []
#while True:
    #soil_value = get_calibrated_soil_moisture()
    #smoothed_value = moving_average(history, soil_value)
    #print(f"Soil Moisture: {smoothed_value:.2f}%")
   # time.sleep(1)
