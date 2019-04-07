# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import pygame

def setVolume(volume):
    if volume >= 0 and volume <=100:
        volumeValue = volume/100.
        pygame.mixer.music.set_volume(volumeValue)
        print('Volume: ' + str(volumeValue))
    else:
        print('Ooops, Please set the valid volume.')

def musicSetup(musicfile, volume):
    pygame.mixer.init()
    pygame.mixer.music.load(musicfile)
    setVolume(volume)

def playBgm():
    pygame.mixer.music.play(-1)

def stopBgm():
    pygame.mixer.music.stop()        

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
musicSetup(musicfile='./music/creativeminds.mp3',volume=10)
while True:
    print("Move the loop to the start rest")
    stopBgm()
    while GPIO.input(start_rest) != 0:
        time.sleep(0.8)
    print("Start when you are ready")
    while GPIO.input(start_rest) == 0:
        time.sleep(0.1)
    playBgm()
    print("Your off")
    penalty = 0
    run_time = time.clock()

    while GPIO.input(end_rest) != 0: 
        if GPIO.input(wire) != 0:
            penalty = penalty + 1
            print("Penalties total", penalty, " points")
            time.sleep(0.07)
        else:
            stopBgm()
            print('Game Over')
            break
    stopBgm()
    score = time.clock() - run_time + (penalty * 0.07)
    print("The run time was " + str(score), " seconds with",penalty, "Penalty points")
