# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import ledlib

def setup():
    GPIO.setmode(GPIO.BCM)

def safeExit():
    GPIO.cleanup()
    exit()

def main():
    try:
        print('The first try of OOP')
        setup()
        gLed = ledlib.Led()
        gLed.turn_on()
        time.sleep(1)
        gLed.turn_off()
        gLed.blink()
        gLed.blink(times=20,frenquency=100)
        safeExit()
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt Detected.')
        safeExit()

main()

