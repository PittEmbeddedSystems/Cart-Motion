#!/usr/bin/env python3

from CartMoveController import CartMoveController
from time import sleep

def main():
    cart = CartMoveController(40)
    cart.turn_left(.25)
    cart.reverse_motion(.5)
    sleep(.3) 
    cart.turn_left(.1)
    cart.reverse_motion(.5)
    sleep(.3) 
    cart.turn_right(.1)
    cart.reverse_motion(.5)
    sleep(.3) 
    cart.turn_left(.1)
    cart.reverse_motion(.5)
    sleep(.3) 
    cart.turn_right(.1)
    cart.reverse_motion(.5)
    sleep(.3) 
    cart.turn_left(.1)
    cart.reverse_motion(.5)
    sleep(.3) 
    

    

if __name__ == "__main__":
    main()
