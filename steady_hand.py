# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Steady Hands game")
delay = range(0,5000)
dum = 0
start_rest = 4
end_rest = 0
wire = 1

while True:
    print("Move the loop to the start rest")
    while GPIO.input(start_rest) != 0:
        time.sleep(0.8)
    print("Start when you are ready")
    while GPIO.input(start_rest) == 0:
        time.sleep(0.1)
    print("Your off")
    penalty = 0
    run_time = time.clock()

    while GPIO.input(end_rest) != 0: 
        if GPIO.input(wire) != 0:
            penalty = penalty + 1
            print("Penalties total", penalty, " points")
            time.sleep(0.07)
        else:
            print('Game Over')
            break
    score = time.clock() - run_time + (penalty * 0.07)
    print("The run time was " + str(score), " seconds with",penalty, "Penalty points")
