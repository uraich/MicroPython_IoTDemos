#!/usr/bin/env python3
# demonstrates a while loop and a for loop

counter = 0
print("while loop:")
while (counter < 5):
    print("The counter is ", counter)
    counter += 1

print("\nfor loop")
for i in range(0,5):
    print(i)
    
# The Fibonacci series
a,b=0,1
print("The Fibonacci series")
while b<200:
    print(b)
    a,b = b, a+b
    
words = ['Tunis','Gaborone','Nairobo','Dakar','Kampala']
for w in words:
    print(w,'has',len(w),'characters')