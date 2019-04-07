# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

class Led:
    self.default_btimes = 10
    self.default_bfrenq = 10
    def __init__(self):
        GPIO.setup(17, GPIO.OUT)

    def turn_on(self):
        GPIO.output(17, True) 

    def turn_off(self):
        GPIO.output(17, False)

    def blink(self,times=self.default_btimes,\
              frenquency=self.default_bfrenq):
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

