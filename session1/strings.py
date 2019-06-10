#!/usr/bin/python3
# string example

# String examples
ais_19 = 'Uganda'                   # using single quotes
ais_19_city = "Kampala"             # using double quotes
ais_19_venue = '''Sheraton Hotel''' # using triple quotes
print(ais_19_city, ais_19, ais_19_venue)

# you have to escape if using single quote in a string enclose in single quotes

ais_19_ug = 'AIS\'19 @ Kampala Uganda'
# or use single quote in a string enclosed in double quotes
ais_19_sh = "AIS\'19 @ Sherator, Kampala Uganda"

print("AIS Host is",ais_19_ug)
print("AIS Venue is",ais_19_sh)

# triple quotes string can extend over multiple lines:
my_string = '''\
Usage: IoTNetwork[Options]
      -h:           display this message
      -H hostname:  name of host to connect to
      '''
print(my_string)

prefix='Py'
postfix='thon'
print(prefix+postfix)

word = 'AFNOG20'
print('word:',word)
print('word[3]:',word[3])
print('word[2:5]:',word[2:5])
print('word[:2]:',word[:5])
print('word[2:]',word[5:])