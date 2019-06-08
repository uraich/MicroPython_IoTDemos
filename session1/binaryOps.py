#!/usr/bin/env python3
# demonstrates binary operators
a = int('00111100',2)
b = int('00001101',2)
print("a & b: ",format(a,'b').zfill(8), "&", format(b,'b').zfill(8)," = ", format(a&b,'b').zfill(8))
print("a | b: ",format(a,'b').zfill(8), "&", format(b,'b').zfill(8)," = ", format(a|b,'b').zfill(8))
print("a ^ b: ",format(a,'b').zfill(8), "&", format(b,'b').zfill(8)," = ", format(a^b,'b').zfill(8))