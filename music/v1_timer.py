# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import pygame
import datetime

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
yongshi = './music/yongshi.mp3'
yi = './music/one.mp3'
er = './music/two.mp3'
san = './music/three.mp3'
si = './music/four.mp3'
wu = './music/five.mp3'
liu = './music/six.mp3'
qi = './music/seven.mp3'
ba = './music/eight.mp3'
jiu = './music/nine.mp3'
shi = './music/ten.mp3'
bai = './music/100.mp3'
fen = './music/fen.mp3'
miao = './music/miao.mp3'
ling = './music/0.mp3'

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
    start_time = datetime.datetime.now()
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
    end_time = datetime.datetime.now()
    total_time =(end_time  - start_time).seconds
    print(total_time)
    stopPlay()
    if happyFlag == True:
        play(endSound,1)
        time.sleep(2)
        ones = total_time%100%10
        tens = total_time%100//10
        huns = total_time//100
        print(huns,tens,ones)
        play(yongshi,1)
        time.sleep(1)
        if huns == 1:
            play(yi,1)
            time.sleep(1)
        elif huns == 2:
            play(er,1)
            time.sleep(1)
        elif huns == 3:
            play(san,1)
            time.sleep(1)
        elif huns == 4:
            play(si,1)
            time.sleep(1)
        elif huns == 5:
            play(wu,1)
            time.sleep(1)
        elif huns == 6:
            play(liu,1)
            time.sleep(1)
        elif huns == 7:
            play(qi,1)
            time.sleep(1)
        elif huns == 8:
            play(ba,1)
            time.sleep(1)
        elif huns == 9:
            play(jiu,1)
            time.sleep(1)
        else:
            pass
        
        if huns > 0:
            play(bai,1)
            time.sleep(1)

        if tens == 1:
            play(yi,1)
        elif tens == 2:
            play(er,1)
        elif tens == 3:
            play(san,1)
        elif tens == 4:
            play(si,1)
        elif tens == 5:
            play(wu,1)
        elif tens == 6:
            play(liu,1)
        elif tens == 7:
            play(qi,1)
        elif tens == 8:
            play(ba,1)
        elif tens == 9:
            play(jiu,1)
        else:
            if huns == 0:
                pass
            else:
                play(ling,1)
        time.sleep(1)
        if huns == 0 and tens == 0:
            pass
        else:
            play(shi,1)
            time.sleep(1)

        
        if ones == 1:
            play(yi,1)
        elif ones == 2:
            play(er,1)
        elif ones == 3:
            play(san,1)
        elif ones == 4:
            play(si,1)
        elif ones == 5:
            play(wu,1)
        elif ones == 6:
            play(liu,1)
        elif ones == 7:
            play(qi,1)
        elif ones == 8:
            play(ba,1)
        elif ones == 9:
            play(jiu,1)
        else:
            pass
        time.sleep(1)
        play(miao,1)
        time.sleep(1)
    else:
        play(badSound,1)
        time.sleep(1.5)
    



