import board
import busio
import digitalio
import adafruit_sdcard
import storage

# Initialize SPI for SD card
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.D5) 
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# Test writing to SD card
with open("/sd/test.txt", "w") as f:
    f.write("Hello, world!\n")

print("Data written to SD card successfully.")
