import board
import analogio
import time

water_level = analogio.AnalogIn(board.VP) 

def get_water_level():
    return (water_level.value/100)

while True:
    water_value = get_water_level()
    print(f"Water Level: {water_value}")
    time.sleep(3)
