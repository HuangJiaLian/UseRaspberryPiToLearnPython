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

def musicSetup(volume):
    pygame.mixer.init()
    setVolume(volume)

def soundSelect(bgmFile,startFile,ooopsFile,endFile):
    #bgm = pygame.mixer.music.load(bgmFile)
    #start = pygame.mixer.music.load(startFile)
    #ooops = pygame.mixer.music.load(ooopsFile)
    #end = pygame.mixer.music.load(endFile)
    bgm = pygame.mixer.Sound(bgmFile)
    start = pygame.mixer.Sound(startFile)
    ooops = pygame.mixer.Sound(ooopsFile)
    end = pygame.mixer.Sound(endFile)
    print(bgm, start,ooops,end)
    return (bgm, start,ooops,end)

def play(soundFile, times):
    bgm = pygame.mixer.music.load(soundFile)
    pygame.mixer.music.play(times)
    

def stopPlay():
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
# musicSetup(cfile='./music/creativeminds.mp3',volume=10)
musicSetup(volume=70)
bgmSound,startSound, ooopsSound, endSound = ('./music/creativeminds_l.mp3', './music/start_ad_01.mp3', './music/ooops_ya_01.mp3', './music/end_fql_01.mp3')
badSound = './music/ooops_ya_02.mp3'

print(bgmSound,startSound,ooopsSound,endSound)
while True:
    print("Move the loop to the start rest")
    stopPlay()
    while GPIO.input(start_rest) != 0:
        time.sleep(0.2)
    print("Start when you are ready")
    play(startSound,5) 
    time.sleep(0.7)
    while GPIO.input(start_rest) == 0:
        time.sleep(0.1)
    play(bgmSound,-1)
    print("Your off")
    penalty = 0
    run_time = time.clock()
    errorCounter = 0
    happyFlag = True
    while GPIO.input(end_rest) != 0: 
        if GPIO.input(wire) != 0:
            penalty = penalty + 1
            print("Penalties total", penalty, " points")
            time.sleep(0.07)
        else:
            # stopPlay()
            play(ooopsSound,1)
            time.sleep(1)
            errorCounter = errorCounter + 1
            happyFlag = False
            print('Game Over')
            break
    stopPlay()
    if happyFlag == True:
        play(endSound,1)
    else:
        play(badSound,1)
    time.sleep(3)
    score = time.clock() - run_time + (penalty * 0.07)
    print("The run time was " + str(score), " seconds with",penalty, "Penalty points")
