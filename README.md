# MicroPython_IoTDemos
Demo programs for the workshop on IoT at the African Internet Summit 2019
## Repository contents
There are 2 categories of programs in this repository:
* hardware access tests
* programs communicating with myDevices Cayenne, publishing results from sensor measurements and accepting commands from Cayenne to drive actuators
Since the ESP8266 uses different pins as compared to the ESP32 each program first checks on which platform it is running (sys.platform is checked to find out)
## Hardware access tests
We have a collection of a dozen different sensor and actuator boards for the WeMos D1 mini system. There are also 2 different types of CPU card, one based on the ESP8266 CPU and the other one based on the ESP32. For each of the sensor boards one or more programs have been written to make sure we can access the features provided by this board, before exposing these features to Cayenne. Here is the list of programs:
* button.py: Reads a simple push button and prints to the screen if the button is currently pushed or not. The switch state is checked once a second
* bmp180Test.py: The BMP180 from Bosch is a barometric pressure sensor with an I2C interface. The program uses the bmp180.py driver module integrated into Micropython to extract temperature, air pressure and altitude. The values are read every 2 s and the result is printed on the screen.
* firstTest.py: The program produces a single tone on the passive buzzer
* espBuzzer.py: The program plays "The Entertainer" tune. For this to work rtttl.py, a program interpreting songs provided in the rtttl (Nokia's Ring Tone Text Transfer Language) as well as songs.py containing tunes desrcibed in rtttl must be uploaded into the lib directory on the WeMos D1 processor flash. Create the lib directory with uPyCraft (if it does not exist) and transfer these files into it.
* ds1307SetTime.py: Sets the time on the DS1307 Real Time Clock (RTC). The time is fixed in the code. You must change it before running the program
* ds1307SetTimeNtp.py: Same as ds1307SetTime, only here the current date and time is read from an NTP server. Just running the program will set the correct time. There is a variable "CET" which, when set to "True" will conver the current time to CET. When set to false, GMT will be used.
* ds1307GetTime.py: Reads the current date and time from the ds1307 RTC and prints it in a humanly readable form
* ds18b20Test.py: Reads the ambient temperature from a Maxim DS18B20 1-wire digital thermometer and prints the result. The ds18b20 driver included in Micropython is used.
* i2cScan.py: Scans the I2C bus for devices connected. It prints the I2C address for each device found.

ledArray: 

* example.py: This is the example provided in the mled library. For it to work animations.py and pixelart.py must be available in the lib directory of the CPU flash. You must define the CPU used when calling the main program (last line in the code)
* matrix.py: Runs through values 0..64 and switches on the number of leds given by this value. The bottom left LED is considered LED 1.
