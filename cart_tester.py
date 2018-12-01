#!/usr/bin/env python3

from CartMoveController import CartMoveController
from time import sleep

def main():
    cart = CartMoveController(40)
    cart.make_a_move(3, 0)
    cart.make_a_move(-3, 0)
    cart.make_a_move(3, 0)
    cart.make_a_move(-3, 0)
    cart.make_a_move(3, 0)
    cart.make_a_move(-3, 0)
    cart.make_a_move(0, -5)
    cart.make_a_move(0, 5)

    

if __name__ == "__main__":
    main()
