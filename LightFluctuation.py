import RPi.GPIO as GPIO
from time import sleep

led_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm = GPIO.PWM(led_pin, 100)
pwm.start(0)

while 1:
	for x in range(100):
		pwm.ChangeDutyCycle(x)
		sleep(0.01)

	for x in range(100, 0, -1):
		pwm.ChangeDutyCycle(x)
		sleep(0.01)
