#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.output(29, GPIO.HIGH)
p = GPIO.PWM(29, 100)

p.start(50)

sleep(10)