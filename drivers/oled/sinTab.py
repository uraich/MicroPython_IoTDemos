#!/usr/bin/python3
# sinCosTab.py
# calculate a sin table for 50 values of angles from 0..2*pi
# The use of the pre-calculated sin and cos values speeds up the drawing
# of circles considerably

from math import sin,cos,pi
sinTab=[]
cosTab=[]
for i in range(0,50):
    sinTab.append(sin(2*pi*i/50))
    cosTab.append(cos(2*pi*i/50))
print("sin table:")
print(sinTab)
print()
print("cos table:")
print(cosTab)
