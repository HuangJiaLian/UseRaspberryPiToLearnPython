# -*- coding: utf-8 -*-
import time # 导入时间模块
import RPi.GPIO as GPIO # 导入GPIO引脚控制模块

GPIO.setmode(GPIO.BCM) # 使用BCM引脚编号模式
GPIO.setup(17, GPIO.OUT) # 设置GPIO17为输出引脚
try:
    counter = 0
    while True:
        GPIO.output(17, True) # LED 亮
        time.sleep(0.25) # 延时0.5秒
        GPIO.output(17, False) # LED 灭
        time.sleep(0.25) # 延时0.5秒
except KeyboardInterrupt:
    print('Exitting ...')
    GPIO.cleanup()

