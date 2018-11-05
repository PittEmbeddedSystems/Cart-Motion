#!/usr/bin/env python

import RPi.GPIO as GPIO
import time 

# Set the mode to GPIO.Board
GPIO.setmode(GPIO.BOARD)

# Output GPIO pins for the left side of the cart
GPIO.setup(32, GPIO.OUT) # IN_1
GPIO.setup(36, GPIO.OUT) # IN_2

# Output GPIO pins for the right side of the cart
GPIO.setup(38, GPIO.OUT) # IN_1
GPIO.setup(40, GPIO.OUT) # IN_2

# Motor Driver Controls
# Counterclockwise - IN_1/IN_2 = LOW/HIGH
# Clockwise - IN_1/IN_2 = HIGH/LOW
# Stop - IN_1/IN_2 = LOW/LOW


# Reverse Motion
def reverse_motion():
	low_channels = [32, 40]
	high_channels = [36, 38]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(2)


#   Forward Motion
# Set 32 and 36 to High/Low respectively for clockwise motion
# Set 38 and 40 to Low/High respectively for counterclockwise motion
def forward_motion():
	low_channels = [36, 38]
	high_channels = [32, 40]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(2)


# All wheels must turn counterclockwise to turn the cart right
def turn_right():
	low_channels = [32, 38]
	high_channels = [36, 40]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(2)


# All wheels must turn clockwise to turn the cart left
def turn_left():
	low_channels = [36, 40]
	high_channels = [32, 38]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(2)

# Stop all cart motion
def stop_motion():
	all_channels=[32, 36, 38, 40]
	GPIO.output(all_channels, GPIO.LOW)


# Drive Forward, then Reverse, then over again
def main():
	forward_motion()
	reverse_motion()

	stop_motion()
	time.sleep(2)

	turn_right()
	turn_left()

	stop_motion()
	time.sleep(2)

	# Cleanup and exit
	GPIO.cleanup()
	exit(0)


if __name__ == "__main__":
	main()
