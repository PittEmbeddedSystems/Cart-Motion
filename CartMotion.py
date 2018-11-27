#!/usr/bin/env python

import RPi.GPIO as GPIO
import time, sys
import pigpio

# Motor Driver Controls
# Counterclockwise - IN_1/IN_2 = LOW/HIGH
# Clockwise - IN_1/IN_2 = HIGH/LOW
# Stop - IN_1/IN_2 = LOW/LOW


###########Front of Cart#############
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#                                   #
#32/36                              #38/40
#                                   #
#                                   #
###########Back of Cart##############



def init():
	# Set the mode to GPIO.Board
	GPIO.setmode(GPIO.BOARD)

	# Output GPIO pins for the left side of the cart
	GPIO.setup(32, GPIO.OUT) # A_IN_1
	GPIO.setup(36, GPIO.OUT) # A_IN_2

	# Output GPIO pins for the right side of the cart
	GPIO.setup(38, GPIO.OUT) # B_IN_1
	GPIO.setup(40, GPIO.OUT) # B_IN_2

	# Output GPIO pins to control the speed of the wheels
	GPIO.setup(35, GPIO.OUT) # PWM

	# Set frequency to 1kHz
	pwm = GPIO.PWM(35, 1000)

	# Set Duty Cycle to 50%
	pwm.start(50)


# Reverse Motion for t seconds
def reverse_motion(t):
	init()

	# Right Wheel Clockwise
	GPIO.output(32, GPIO.LOW)
	GPIO.output(36, GPIO.HIGH)

	# Left Wheel CCL
	GPIO.output(38, GPIO.HIGH)
	GPIO.output(40, GPIO.LOW)

	time.sleep(t)
	GPIO.cleanup()


#   Forward Motion for t seconds
#   Right spins clockwise, left counterclockwise
def forward_motion(t):
	init()

	# Right Wheel Clockwise
	GPIO.output(32, GPIO.HIGH)
	GPIO.output(36, GPIO.LOW)

	# Left Wheel CCL
	GPIO.output(38, GPIO.LOW)
	GPIO.output(40, GPIO.HIGH)

	time.sleep(t)
	GPIO.cleanup()


# All wheels must turn counterclockwise to turn the cart right for t seconds
def turn_right(t):
	init()

	# Right Wheel CCL
	GPIO.output(32, GPIO.LOW)
	GPIO.output(36, GPIO.HIGH)

	# Left Wheel CCL
	GPIO.output(38, GPIO.LOW)
	GPIO.output(40, GPIO.HIGH)

	time.sleep(t)
	GPIO.cleanup()


# All wheels must turn clockwise to turn the cart left for t seconds
def turn_left(t):
	init()

	# Right Wheel Clockwise
	GPIO.output(32, GPIO.HIGH)
	GPIO.output(36, GPIO.LOW)

	# Left Wheel Clockwise
	GPIO.output(38, GPIO.HIGH)
	GPIO.output(40, GPIO.LOW)

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
	forward_motion(10)

	# Drive backward
	#reverse_motion(1)

	# Turn right
	#turn_right(2)

	# Turn left
	#turn_left(2)

	exit(0)


if __name__ == "__main__":
	main()
