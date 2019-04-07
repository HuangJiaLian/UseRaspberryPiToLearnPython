# -*- coding: utf-8 -*-
import pygame
import time
import RPi.GPIO as GPIO

# Set the valume between 0 to 100
def setVolume(volume):
    if volume >= 0 and volume <=100:
        volumeValue = volume/100.
        pygame.mixer.music.set_volume(volumeValue)
        print('Volume: ' + str(volumeValue))
    else:
        print('Ooops, Please set the valid volume.')

def getVolume():
    volumeValue = 100.*pygame.mixer.music.get_volume()
    return volumeValue

def volumeUp(stepSize):
    if stepSize <=0 :
        print('Oooops, Please give the valid stepsize')
        return False

    currentVolume = getVolume()
    newVolume = -1
    if currentVolume + stepSize > 100:
        newVolume = 100
    else:
        newVolume = currentVolume + stepSize
    setVolume(newVolume)
    return True

def volumeDown(stepSize):
    if stepSize <=0 :
        print('Oooops, Please give the valid stepsize')
        return False

    currentVolume = getVolume()
    newVolume = -1
    if currentVolume - stepSize < 0:
        newVolume = 0
    else:
        newVolume = currentVolume - stepSize
    setVolume(newVolume)
    return True

def musicSetup(musicfile, looptimes, volume):
    pygame.mixer.init()
    pygame.mixer.music.load(musicfile)
    pygame.mixer.music.play(looptimes)
    setVolume(volume)

def pinSetup():
    GPIO.setmode(GPIO.BCM) # 设定采用的引脚模式
    GPIO.setup(17, GPIO.OUT) # 设置与LED相连的引脚: GPIO17为输出引脚
    # 设置与Button相连的两个引脚为输入引脚，上拉模式
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 输入引脚状态读取函数
def readPinStatus(pinNum):
    status = GPIO.input(pinNum)
    return status

# 判断是否有键被按下
def buttonPressed(button1_state, button2_state):
    return (button1_state == False or button2_state == False)


def main():
    musicSetup(musicfile='./music/creativeminds.mp3', looptimes=2, volume=10)
    pinSetup()
    try:
        while True:
            button1_state = readPinStatus(27)
            button2_state = readPinStatus(22)
            if buttonPressed(button1_state,button2_state):
                if button1_state == False:
                    volumeUp(5)
                    time.sleep(0.2)
                else:
                    volumeDown(5)
                    time.sleep(0.2)
            else:
                time.sleep(0.2)
    except KeyboardInterrupt:
        print('Exiting safely ...')
        GPIO.cleanup()

main()
