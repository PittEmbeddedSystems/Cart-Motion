#!/usr/bin/env python

import RPi.GPIO as GPIO
import time 

# Set the mode to GPIO.Board
GPIO.setmode(GPIO.BOARD)

# Output GPIO pins for the right side of the card
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

# Output GPIO pins for the left side of the cart
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)


# Reverse Motion #
# Set 38 and 40 to High/Low respectively for clockwise motion
# Set 32 and 36 to Low/High respectively for counterclockwise motion
def reverse_motion():
	low_channels = [32, 40]
	high_channels = [36, 38]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(5)


#   Forward Motion   #
# Set 32 and 36 to High/Low respectively for clockwise motion
# Set 38 and 40 to Low/High respectively for counterclockwise motion
def forward_motion():
	low_channels = [36, 38]
	high_channels = [32, 40]
	GPIO.output(low_channels, GPIO.LOW)
	GPIO.output(high_channels, GPIO.HIGH)
	time.sleep(5)

# TODO
# Right wheels will need to spin counterclockwise
# Left wheels will need to spin clockwise
def turn_right():
	low_channels = []
	high_channels = []
	return

# TODO
# Right wheels will need to spin counterclockwise
# Left wheels will need to spin clockwise
def turn_left():
	low_channels = []
	high_channels = []
	return


def stop_motion():
	all_channels=[32, 36, 38, 40]
	GPIO.output(all_channels, GPIO.LOW)

# Drive Forward, then Reverse, then over again
def main():
	forward_motion()
	reverse_motion()

	stop_motion()

	forward_motion()
	reverse_motion()

	stop_motion()

	# Cleanup and exit
	GPIO.cleanup()
	exit(0)


if __name__ == "__main__":
	main()
