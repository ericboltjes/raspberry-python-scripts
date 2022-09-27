#!/usr/bin/env python

import math # Used to convert float to integer
import bme280 # Library for the BME280 sensor
import tm1637 # Library for the 7 segment display

# These vars define the GPIO pins used for the display
CLK = 21
DIO = 20

tm = tm1637.TM1637(clk=CLK, dio=DIO)

def main():

    while True:

        # Setup the Sensor to collect data
        bme = bme280.Bme280()
        bme.set_mode(bme280.MODE_FORCED)
        
        # Get data from the sensor t = temperature, p = pressure and h = humidity
        t, p, h = bme.get_data()
        
        # Convert temperature float value to integer to make it compatible with the display
        temp = math.trunc(t)
        
        # Show the Temperature with °c on the display
        tm.temperature(temp)

# Start the code execution
if __name__ == '__main__':
    main()
