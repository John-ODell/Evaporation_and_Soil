Evaporation of Water compare to Water in Soil by John O'Dell 

Items Needed

    - ESP-WROOM-32S (Not tested on Other Devices, Should work in theory) 
    - Water Level Sensor
    - Soil Moisture Sensor
    - DHT 11
    - .96 OLED Screen
    - TF Micro-SD card Module
    - Adafriut-CircuitPython-Libraries-9x
    - Thony IDE 

Flashing CircuitPython

    - Download Thonny IDE
    - Navigate to Run on the top left
        - Configure Interpreter 
        - epstool (middle bottom right blue color)
            - Target Port
                - COMS 
            - CircuitPython Family
                - Check your board (ESP32 for this example)
            Variant
                - Check the manifacturer
            Version
                - Most recent/9.x.x release
    - Click install
    - Exit out of the current screen and back to Configure Interpreter
        - Which Kind
            - CircuitPython (Generic)
        - Port 
            - COMS (this port may have changed after flashing)
    - Press OK

CircuitPython Libraries and MPY Dependicies 

To your left on thonny you will see the folders of your device and you computer.
Open the lib folder (double click) of the device and navigate to your CircuitPython 9x libraries in the folder above

    - Inside CircuitPython 9x lib click and press Download into the ESP lib folder
        - adafruit_bus_device (folder)
        - adafruit_register (folder)
        - adafruit_sdcard.mpy (file)
        - adafruit_dht11.mpy (file)
    - You must have these on your device or the sd card and dht 11 will not work.

Pin Connections
Soil Moisture Sensor:

    - S/AO -> GPIO39 (A1)
    - VCC -> 3.3v
    - GND -> GND

Water Level Sensor:

    - S/AO -> GPIO34 (A2)
    - VCC -> 3.3v
    - GND -> GND

TF SD Card Module:

    - MISO -> GPIO19
    - MOSI-> GPIO23
    - SCK-> GPIO18
    - CS -> GPIO5
    - VCC -> 3.3v (We use 3.3v for the esp unlike 5v for the pi pico's)
    - GND -> GND

DHT 11

    - S/DO -> D4 GPIO4
    - VCC ->
    - GND ->

SOIL MOISTURE MODULE 

Soil Moisture Sensor Pins:

    - S/AO -> GPIO39 (A1)
    - VCC -> 3.3v
    - GND -> GND

Open up the file "Soil_Moisture_Example" and press the green arrow

    - hold the Soil Moisture Module dry for a couple of seconds
    - hold the Soil Moisture Module completely in water for a couple of seconds
    - press the red stop button
    - notate the Max and Min values return when the module was wet/dry

Open the file "Soil_Moisture_Calibration"

    - take the max and min value recorded and replace
        - DRY_VALUE = MAX_VALUE 
        - WET_VALUE = MIN_VALUE
            - Dry off the module
    - run file and test the module 
    - calibration may take multipletest

PLEASE CALIBRATE YOUR UNIT FOR AN ACCURATE TEST

WATER SENSOR MODULE
Water_Sensor_Example

Water Level Sensor Pins:

    - S/AO -> GPIO34 (A2)
    - VCC -> 3.3v
    - GND -> GND

Open the file "Water_Sensor_Example" and press the green arrow

    - get room temperature water
    - take a dry sample
    - place the module fully to the 4 line
        -take a few reading
    - dry off and place at the 2 line
    - dry off and take a dry sample
    - these resuts can be hard to read, feel free adjust the math to your liking.

DHT11 TEMPERATURE AND HUMIDITY MODULE
DHT11 example

DHT 11

    - S/DO -> D4 GPIO4
    - VCC ->
    - GND -

Open the file "DHT11_evaporation_example" and press the green arrow
    - The temperature in celsius, fahrenheit and the humidity percentage will return in the serial shell

TF MICRO SD CARD MODULE
SD card init example

TF SD Card Module:

    - MISO -> GPIO19
    - MOSI-> GPIO23
    - SCK-> GPIO18
    - CS -> GPIO5
    - VCC -> 3.3v 
    - GND -> GND

Format a Micro-SD card in a fat32 format (32gb or less preffered)
open the file "sd_init" and press the green arrow

    - press the red stop button
    - when clicking on the SD folder in thonny, no file may apper
    - removing the sd card and reading it you will find your file
    - you do not need to delete this file 

MAKE SURE ALL EXAMPLES ARE WORKING BEFORE RUNNING THE MAIN BOOT.
A FILE NAMED BOOT.PY WILL MAKE THE ESP RUN ON BOOT, CHANGE THE NAME IF YOU WOULD LIKE TO USE THIS LIKE AN EXAMPLE

open the file "boot.py"

    - file 
        - save as 
            - this device
                - "boot.py"
    - hit the green arrow

Every Hour Each sensor records their wate level and along with the temperature in fahrenheit, celsius, and the humitidy and saves it the micro sd in a csv format.

After First reading, Timestamps did not record correctly. I will try to correct this, but it may be another required lib. For now, Mark down the start time and check out the Juypter Notebook for time correction Code.  (No Need to hand write in excel)

Mix soil well, try not to disturb the water.
Pour the water at room Temp. 
You may need to mix up the soil during data recording so it wont harden. 