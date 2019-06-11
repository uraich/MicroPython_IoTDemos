#!/usr/bin/env python3
# demonstrate how variables are allocated
a=5
print("a is of",type(a), "and has the value",a)
b=7.4
print("b is of",type(b), "and has the value",b)
hello="Hello World"
print("hello is of",type(hello), "and has the value",hello)
h=b'Hello World'
print("h is of",type(h), "and has the value",h)
ready = True
print("ready is of",type(ready), "and has the value",ready)
c = complex(3,6)
print("c is of",type(c), "and has the value",c)
cars=('honda','fiat','porsche','mercedes','ferrari')
print("cars is of",type(cars), "and has the value",cars)
l=[0,1,2,3,5,7,11]
print("l is of",type(l), "and has the value",l)
r = range(0,5)
print("r is of",type(r),"and has the value",r)
shoppingList = {
    "fruit": "banana",
    "staplefood": "rice",
    "bread": "baguette",
    "drink": "beer"
} 

print("shoppingList is of type",type(shoppingList), "and has the value",shoppingList)