# -*- coding: utf-8 -*-
import time # 导入时间模块
import RPi.GPIO as GPIO # 导入GPIO引脚控制模块

GPIO.setmode(GPIO.BCM) # 使用BCM引脚编号模式
GPIO.setup(17, GPIO.OUT) # 设置GPIO17为输出引脚

counter = 0
while counter < 4:
    GPIO.output(17, True) # LED 亮
    time.sleep(0.5) # 延时0.5秒
    GPIO.output(17, False) # LED 灭
    time.sleep(0.5) # 延时0.5秒
    counter = counter + 1
GPIO.cleanup()

