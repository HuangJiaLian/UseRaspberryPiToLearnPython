# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

class LED:
    def __init__(self):
        self.color = 'green'
        self.size = 'little'
        self.setup()

    def setup(self):
        GPIO.setup(17, GPIO.OUT)

    def show_info(self):
        print(self.color, self.size)

    def turn_on(self):
        GPIO.output(17, True) 

    def turn_off(self):
        GPIO.output(17, False)

    def blink(self, times, frenquency):
        if times <= 0 or frenquency <=0:
            print('Oooops, please give the \
                  right times or frequency')
            return
        else:
            period = 1./frenquency
            for i in range(times):
                self.turn_on()
                time.sleep(period/2.)
                self.turn_off()
                time.sleep(period/2.)


def setup():
    GPIO.setmode(GPIO.BCM)

def safeExit():
    GPIO.cleanup()
    exit()

def main():
    try:
        print('The first try of OOP')
        setup()
        gLed = LED()
        gLed.show_info()
        gLed.turn_on()
        time.sleep(1)
        gLed.turn_off()
        gLed.blink(times=20,frenquency=20)
        safeExit()
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt Detected.')
        safeExit()

main()