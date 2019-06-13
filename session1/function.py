#!/usr/bin/env python3
# demo on how to define and use functions

# a global variable
total=0
# the function definition
def sum(num1,num2):
    total=num1+num2
    print("Total inside the function:",total)
    print("The sum of {:.2f} and {:.2f} is {:.2f}".format(num1,num2,total))
    return total

print("The sum of 10+20 is ",sum(10,20))
print("total outside the function:",total)