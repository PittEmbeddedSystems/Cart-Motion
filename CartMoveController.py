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

        # We made these measurements empirically so they're kind of magical
        self._turning_duty_cycle = 40
        self._degrees_per_second = 16
        self._straight_duty_cycle = 20
        self._cm_per_second = 7

    def __del__(self):
        self.pwm = 0
        GPIO.cleanup()

    def make_a_move(self, turn_angle, driving_distance):
        """
        This method initiates a movement action from the cart. It accepts a
        turning angle in degrees and a driving distance in cm. Upon running this
        method the cart will first rotate itself in accordance with the turn_angle
        and then it will drive either directly forward or directly backward based
        on the driving_distance. Forward for positive distances, reverse for 
        negative distances.

        NOTE: This method expects turn_angles to be in the range [-180, 180)
        """

        if turn_angle < 0:
            self.turn_left(-1 * turn_angle)
        else if turn_angle > 0:
            self.turn_right(turn_angle)

        if driving_distance > 0:
            self.forward_motion(driving_distance)
        else
            self.reverse_motion(driving_distance)
        pass

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


        self.pwm.ChangeDutyCycle(self._turning_duty_cycle)
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
        self.pwm.ChangeDutyCycle(self._turning_duty_cycle)
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

