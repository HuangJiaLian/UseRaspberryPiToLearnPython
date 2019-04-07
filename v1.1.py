# -*- coding: utf-8 -*-
# Write Winner Record
import RPi.GPIO as GPIO
import time
import pygame
import cowsay
from datetime import datetime as dt

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


def play(soundFile, times):
    bgm = pygame.mixer.music.load(soundFile)
    pygame.mixer.music.play(times)
    

def stopPlay():
    pygame.mixer.music.stop()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print('#############################')
print('   Use Pi To Learn Python    ')
print('     Steady Hands            ')
print('#############################')

cowsay.cow('Steady Hands')
dum = 0
start_rest = 4
end_rest = 0
wire = 1


musicSetup(volume=30)
bgmSound = './music/creativeminds_l.mp3'
startSound = './music/start_ad_01.mp3'
ooopsSound = './music/ooops_ya_01.mp3'
endSound = './music/end_fql_01.mp3'
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
bai = './music/bai.mp3'
fen = './music/fen.mp3'
miao = './music/miao.mp3'
ling = './music/0.mp3'

while True:
    print("Move the loop to the start rest")
    stopPlay()
    while GPIO.input(start_rest) != 0:
        time.sleep(0.2)
    print("Start when you are ready")
    play(startSound,5) 
    time.sleep(0.7)
    while GPIO.input(start_rest) == 0:
        time.sleep(0.01)
    play(bgmSound,-1)
    print("Your off")
    start_time = time.time() 
    errorCounter = 0
    happyFlag = True
    while GPIO.input(end_rest) != 0: 
        if GPIO.input(wire) != 0:
            time.sleep(0.01)
        else:
            # stopPlay()
            play(ooopsSound,1)
            time.sleep(1)
            errorCounter = errorCounter + 1
            happyFlag = False
            print('Game Over')
            break
    total_time = time.time() - start_time
    print(total_time)
    mini_time = str(round(total_time - int(total_time),2))
    total_time_int = int(total_time)
    stopPlay()
    if happyFlag == True:
        winDate = str(dt.today())
        logfile = open('record.csv', 'a')
        logfile.write(str(round(total_time,2)) + ' ' + winDate + '\n')
        logfile.close()
        play(endSound,1)
        time.sleep(2)
        ones = total_time_int%100%10
        tens = total_time_int%100//10
        huns = total_time_int//100
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
            if huns == 0:
                pass
            else:
                play(yi,1)
                time.sleep(1)
        elif tens == 2:
            play(er,1)
            time.sleep(1)
        elif tens == 3:
            play(san,1)
            time.sleep(1)
        elif tens == 4:
            play(si,1)
            time.sleep(1)
        elif tens == 5:
            play(wu,1)
            time.sleep(1)
        elif tens == 6:
            play(liu,1)
            time.sleep(1)
        elif tens == 7:
            play(qi,1)
            time.sleep(1)
        elif tens == 8:
            play(ba,1)
            time.sleep(1)
        elif tens == 9:
            play(jiu,1)
            time.sleep(1)
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
            time.sleep(1)
        elif ones == 2:
            play(er,1)
            time.sleep(1)
        elif ones == 3:
            play(san,1)
            time.sleep(1)
        elif ones == 4:
            play(si,1)
            time.sleep(1)
        elif ones == 5:
            play(wu,1)
            time.sleep(1)
        elif ones == 6:
            play(liu,1)
            time.sleep(1)
        elif ones == 7:
            play(qi,1)
            time.sleep(1)
        elif ones == 8:
            play(ba,1)
            time.sleep(1)
        elif ones == 9:
            play(jiu,1)
            time.sleep(1)
        else:
            pass
        play(miao,1)
        time.sleep(1)
        # Play mini time
        if mini_time[-2] == '1':
            play(yi,1)
        elif mini_time[-2] == '2':
            play(er,1)
        elif mini_time[-2] == '3':
            play(san,1)
        elif mini_time[-2] == '4':
            play(si,1)
        elif mini_time[-2] == '5':
            play(wu,1)
        elif mini_time[-2] == '6':
            play(liu,1)
        elif mini_time[-2] == '7':
            play(qi,1)
        elif mini_time[-2] == '8':
            play(ba,1)
        elif mini_time[-2] == '9':
            play(jiu,1)
        elif mini_time[-2] == '0':
            play(ling,1)
        else:
            pass
        time.sleep(1)

        if mini_time[-1] == '1':
            play(yi,1)
        elif mini_time[-1] == '2':
            play(er,1)
        elif mini_time[-1] == '3':
            play(san,1)
        elif mini_time[-1] == '4':
            play(si,1)
        elif mini_time[-1] == '5':
            play(wu,1)
        elif mini_time[-1] == '6':
            play(liu,1)
        elif mini_time[-1] == '7':
            play(qi,1)
        elif mini_time[-1] == '8':
            play(ba,1)
        elif mini_time[-1] == '9':
            play(jiu,1)
        elif mini_time[-1] == '0':
            play(ling,1)
        else:
            pass
        time.sleep(1)
    else:
        pass
    



