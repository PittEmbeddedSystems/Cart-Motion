import time
import RPi.GPIO as GPIO

class CartMoveController(object):
    def __init__(self, speed):
        self.speed = speed
        # Set the mode to GPIO.Board
        GPIO.setmode(GPIO.BOARD)

        # Output GPIO pins for the left side of the cart
        GPIO.setup(32, GPIO.OUT) # A_IN_1
        GPIO.setup(36, GPIO.OUT) # A_IN_2

        # Output GPIO pins for the right side of the cart
        GPIO.setup(40, GPIO.OUT) # B_IN_1
        GPIO.setup(38, GPIO.OUT) # B_IN_2

        # Output GPIO pins to control the speed of the wheels
        GPIO.setup(29, GPIO.OUT) # PWM

        # Set pin high
        GPIO.output(29, GPIO.HIGH)

        # Set frequency to 1kHz
        self.pwm = GPIO.PWM(29, 1000)

        # After relating speed to duty cycle
        self.pwm.start(speed)

    def __del__(self):
        self.pwm = 0
        GPIO.cleanup()

    #   Forward Motion for t seconds
    #   Right spins clockwise, left counterclockwise
    def forward_motion(self, move_duration_secs):

        self.pwm.ChangeDutyCycle(20)
        # Right Wheel Clockwise
        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)

        # Left Wheel CCL
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(38, GPIO.LOW)

        time.sleep(move_duration_secs)
        self.halt_motion()


    # Reverse Motion for t seconds
    def reverse_motion(self, move_duration_secs):
        self.pwm.ChangeDutyCycle(20)
        # Right Wheel Clockwise
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)

        # Left Wheel CCL
        GPIO.output(40, GPIO.LOW)
        GPIO.output(38, GPIO.HIGH)

        time.sleep(move_duration_secs)
        self.halt_motion()

    # All wheels must turn clockwise to turn the cart left for t seconds
    def turn_left(self, move_duration_secs):


        self.pwm.ChangeDutyCycle(40)
        # Right Wheel CCL
        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)

        # Left Wheel CCL
        GPIO.output(40, GPIO.LOW)
        GPIO.output(38, GPIO.HIGH)

        time.sleep(move_duration_secs)
        self.halt_motion()

    # All wheels must turn counterclockwise to turn the cart right for t seconds
    def turn_right(self, move_duration_secs):
        self.pwm.ChangeDutyCycle(40)
        # Right Wheel Clockwise
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)

        # Left Wheel Clockwise
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(38, GPIO.LOW)

        time.sleep(move_duration_secs)
        self.halt_motion()

    def halt_motion(self):
        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)

