#!/usr/bin/python3
# List examples

list1= ['Senegal', 'Uganda', 2018, 2019]
list2=[1,2,3,4,5];
list3=["a","b","c","d"]

# Accessing list elements

print("list1[0]:",list1[0])
print("list2[1:5]:",list2[1:5])
print("list3: ",list3)
# updating lists

list4 = ['South Africa', 'Ghana', 1999, 2001];
print ('list4[0] and list4[2]:',list4[0],list4[2])
list4[2] = 2000
print ('updated list4[0] and list4[2]:',list4[0],list4[2])

# some methods of the list class
print("Length of list4:",len(list4))
print("list2: ",list2)
print("Max value in list2:",max(list2))

seq = ('South Africa', 'Ghana', 1999, 2001,'Senegal','Uganda', 2018, 2019)
print("seq is a ",type(seq), "with value:",seq)
list5 = list(seq)
print("list5 is a ",type(list5), "with value:",list5)