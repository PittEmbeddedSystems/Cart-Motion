#!/usr/bin/env python

import RPi.GPIO as GPIO
import time 

# Motor Driver Controls
# Counterclockwise - IN_1/IN_2 = LOW/HIGH
# Clockwise - IN_1/IN_2 = HIGH/LOW
# Stop - IN_1/IN_2 = LOW/LOW


def init():
	# Set the mode to GPIO.Board
	GPIO.setmode(GPIO.BOARD)

	# Output GPIO pins for the left side of the cart
	GPIO.setup(32, GPIO.OUT) # IN_1
	GPIO.setup(36, GPIO.OUT) # IN_2

	# Output GPIO pins for the right side of the cart
	GPIO.setup(38, GPIO.OUT) # IN_1
	GPIO.setup(40, GPIO.OUT) # IN_2


# Reverse Motion for t seconds
def reverse_motion(t):
	init()
	low_channels = [32, 40]
	high_channels = [36, 38]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(t)
	GPIO.cleanup()


#   Forward Motion for t seconds
def forward_motion(t):
	init()
	low_channels = [36, 38]
	high_channels = [32, 40]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(t)
	GPIO.cleanup()


# All wheels must turn counterclockwise to turn the cart right for t seconds
def turn_right(t):
	init()
	low_channels = [32, 38]
	high_channels = [36, 40]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(t)
	GPIO.cleanup()


# All wheels must turn clockwise to turn the cart left for t seconds
def turn_left(t):
	init()
	low_channels = [36, 40]
	high_channels = [32, 38]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(t)
	GPIO.cleanup()

# Stop all cart motion for t seconds
def stop_motion(t):
	init()
	all_channels = [32, 36, 38, 40]
	GPIO.output(all_channels, GPIO.LOW)
	time.sleep(t)
	GPIO.cleanup()


# Drive Forward, then Reverse, then over again
def main():
	# Drive forward
	forward_motion(2)

	# Drive backward
	reverse_motion(2)

	# Stop
	stop_motion(2)

	# Turn right
	turn_right(5)

	# Turn left
	turn_left(5)

	# Stop
	stop_motion(2)

	exit(0)


if __name__ == "__main__":
	main()
