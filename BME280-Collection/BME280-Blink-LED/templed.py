#!/usr/bin/env python

import math
import bme280
import RPi.GPIO as GPIO
from time import sleep

yellowLedPin = 7
blueLedPin = 11
greenLedPin = 13

def lighton():
    while True:
        bme = bme280.Bme280()
        bme.set_mode(bme280.MODE_FORCED)
        t, p, h = bme.get_data()
        temp = math.trunc(t)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(yellowLedPin, GPIO.OUT)
        GPIO.setup(blueLedPin, GPIO.OUT)
        GPIO.setup(greenLedPin, GPIO.OUT)
        if temp > 28:
                GPIO.output(blueLedPin, GPIO.LOW)
                GPIO.output(greenLedPin, GPIO.LOW)
                GPIO.output(yellowLedPin, GPIO.HIGH)
        if 25 < temp <= 28:
                GPIO.output(yellowLedPin, GPIO.LOW)
                GPIO.output(greenLedPin, GPIO.LOW)
                GPIO.output(blueLedPin, GPIO.HIGH)
        if temp <= 25:
                GPIO.output(yellowLedPin, GPIO.LOW)
                GPIO.output(blueLedPin, GPIO.LOW)
                GPIO.output(greenLedPin, GPIO.HIGH)
def lightoff():
    GPIO.output(blueLedPin, GPIO.LOW)
    GPIO.output(yellowLedPin, GPIO.LOW)
    GPIO.output(greenLedPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        lighton()

    except KeyboardInterrupt:
        lightoff()
