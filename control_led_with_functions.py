# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO # GPIO引脚库
import time # 用来控制时间

################################
# 1. 函数定义
################################
# 引脚初始化函数
def setup():
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

# LED闪烁函数
def blink(speed, times):
    counter = 0
    t = 1./speed/2.
    while counter < times:
        GPIO.output(17, True)
        time.sleep(t)
        GPIO.output(17, False)
        time.sleep(t)
        counter = counter + 1

# 安全退出函数
def safeExit():
    print('Exiting ...')
    GPIO.cleanup()

# 主函数
def main():
    setup()
    try:
        while True:
            button1_state = readPinStatus(27)
            button2_state = readPinStatus(22)
            if buttonPressed(button1_state,button2_state):
                if button1_state == False:
                    blink(5,50)
                else:
                    blink(10,50)
            else:
                time.sleep(0.2)
    except KeyboardInterrupt:
        safeExit()


#######################################
# 函数调用
#######################################
main()