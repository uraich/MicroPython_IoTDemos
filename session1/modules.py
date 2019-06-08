#!/usr/bin/env python3
# demonstrates the use of the math modules

from math import sin,radians,pi

def sinDeg(degrees):
    return sin(radians(degrees))
                    
print("sin(30): ",sinDeg(30))
print("sin(pi/6): ",sin(pi/6))