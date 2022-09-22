#!/usr/bin/env python

import math
import bme280
import tm1637
from time import sleep

CLK = 21
DIO = 20
DELAY = 0.1

tm = tm1637.TM1637(clk=CLK, dio=DIO)

def main():

    while True:

        bme = bme280.Bme280()
        bme.set_mode(bme280.MODE_FORCED)
        t, p, h = bme.get_data()
        temp = math.trunc(t)
        tm.temperature(temp)

if __name__ == '__main__':
    main()
