from RPi.GPIO import GPIO

class CartMoveController(object):
    def __init__(self, speed):
        self.speed = speed
        # Set the mode to GPIO.Board
        GPIO.setmode(GPIO.BOARD)

        # Output GPIO pins for the left side of the cart
        GPIO.setup(32, GPIO.OUT) # A_IN_1
        GPIO.setup(36, GPIO.OUT) # A_IN_2

        # Output GPIO pins for the right side of the cart
        GPIO.setup(38, GPIO.OUT) # B_IN_1
        GPIO.setup(40, GPIO.OUT) # B_IN_2

        # Output GPIO pins to control the speed of the wheels
        GPIO.setup(29, GPIO.OUT) # PWM

        # Set pin high
        GPIO.output(29, GPIO.HIGH)

        # Set frequency to 1kHz
        pwm = GPIO.PWM(29, 1000)

        # After relating speed to duty cycle
        pwm.start(speed)
        
    def __del__(self):
        GPIO.cleanup()
        
    # Reverse Motion for t seconds
    def reverse_motion(self, t):

        # Right Wheel Clockwise
        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)

        # Left Wheel CCL
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)

        time.sleep(t)


    #   Forward Motion for t seconds
    #   Right spins clockwise, left counterclockwise
    def forward_motion(self, t):

        # Right Wheel Clockwise
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)

        # Left Wheel CCL
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.HIGH)

        time.sleep(t)



    # All wheels must turn counterclockwise to turn the cart right for t seconds
    def turn_right(self, t):

        # Right Wheel CCL
        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)

        # Left Wheel CCL
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.HIGH)

        time.sleep(t)



    # All wheels must turn clockwise to turn the cart left for t seconds
    def turn_left(self, t):

        # Right Wheel Clockwise
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)

        # Left Wheel Clockwise
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)

        time.sleep(t)
