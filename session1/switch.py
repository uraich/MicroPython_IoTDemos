#!/usr/bin/env
# using a dictionary to implement a switch/case statement

 
def zero():
    print(" You typed zero\n")
 
def sqr():
    print(" is a perfect square\n")
 
def even():
    print(" is an even number\n")
 
def prime():
    print(" is a prime number\n")
    
options = {0 : zero,
                1 : sqr,
                4 : sqr,
                9 : sqr,
                2 : even,
                3 : prime,
                5 : prime,
                6 : even,
                7 : prime,
}

for i in range (0,8):
    print(i,end='')
    options[i]()