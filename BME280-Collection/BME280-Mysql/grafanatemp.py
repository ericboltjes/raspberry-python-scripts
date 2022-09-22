#!/usr/bin/env python

import math
import bme280
import tm1637
import mysql.connector
from datetime import datetime
from time import sleep

CLK = 21
DIO = 20
DELAY = 1

tm = tm1637.TM1637(clk=CLK, dio=DIO)

conn = mysql.connector.connect(user='root', password='tbssi21a', host='127.0.0.1', database='grafana')

cursor = conn.cursor()

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def main():

    while True:

        bme = bme280.Bme280()
        bme.set_mode(bme280.MODE_FORCED)
        t, p, h = bme.get_data()

        pressure = (p/100)
        pressstring = str(pressure)
        tempstring = str(t)
        humstring = str(h)
        timestring = str(current_time())
        timestring = '"' + str(timestring) + '"'
        sqltemp = 'INSERT INTO TempGraph (Temp, Time) VALUES ('+ tempstring +', '+ timestring +')'
        sqlhum = 'INSERT INTO HumidityGraph (Hum, Time) VALUES ('+ humstring +', '+ timestring +')'
        sqlpress = 'INSERT INTO PressureGraph (Press, Time) VALUES ('+ pressstring +', '+ timestring +')'
        try:
           cursor.execute(sqltemp)
           conn.commit()
        except:
           conn.rollback()

        try:
           cursor.execute(sqlhum)
           conn.commit()
        except:
           conn.rollback()

        try:
           cursor.execute(sqlpress)
           conn.commit()
        except:
           conn.rollback()
        sleep(DELAY)

if __name__ == '__main__':
    main()
