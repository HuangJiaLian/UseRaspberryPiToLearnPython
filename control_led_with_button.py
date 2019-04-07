# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO # GPIO引脚库
import time # 用来控制时间


GPIO.setmode(GPIO.BCM) # 设定采用的引脚模式
GPIO.setup(17, GPIO.OUT) # 设置与LED相连的引脚: GPIO17为输出引脚

# 设置与Button相连的两个引脚为输入引脚，上拉模式
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    # 读取两个输入引脚的状态
    button1_state = GPIO.input(27)
    button2_state = GPIO.input(22)
    # 判断是否有button被按下
    if button1_state == False or button2_state == False: # 有Button被按下
        print('Button Pressed')
        # 判断是哪一个键被按下
        if button1_state == False: # 第一个Button被按下
            # 慢闪50下
            counter1 = 0
            t = 1./5./2.
            while counter1 < 50:
                GPIO.output(17, True)
                time.sleep(t)
                GPIO.output(17, False)
                time.sleep(t)
                counter1 = counter1 + 1
        else:# 第二个Button被按下
            # 快闪50下
            counter2 = 0
            t = 1./10./2.
            while counter2 < 50:
                GPIO.output(17, True)
                time.sleep(t)
                GPIO.output(17, False)
                time.sleep(t)
                counter2 = counter2 + 1
    else:
        time.sleep(0.2)
