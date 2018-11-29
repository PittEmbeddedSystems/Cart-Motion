#!/usr/bin/env python3

from CartMoveController import CartMoveController

def main():
    cart = CartMoveController(50)
    cart.reverse_motion(10)
    

if __name__ == "__main__":
    main()