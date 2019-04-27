# Test for sdcard block protocol
# Peter hinch 30th Jan 2016
# adapted to the WeMos D1 mini by Uli Raich
import sys, os, sdcard, machine

SPI_CS = 15

def sdtest():
    print("SD card test")
    spi = machine.SPI(1)
    spi.init()  # Ensure right baudrate
    sd = sdcard.SDCard(spi, machine.Pin(SPI_CS)) # ESP8266 version
    print("Sd card created")
    try:
        os.mount(sd, '/sd')
    except:
        print("Cannot mount file system on sd card")
        sys.exit()
    print('Filesystem check')
    print(os.listdir('/sd'))

    line = 'abcdefghijklmnopqrstuvwxyz\n'
    lines = line * 50 # 1350 chars
    short = '1234567890\n'
    fn = '/sd/rats.txt'
    if 'rats.txt' in os.listdir('/sd'):
        print("%s exists, deleting it"%fn)
        os.remove("/sd/rats.txt")
    
    print()
    print('Multiple block read/write')
    
    with open(fn,'w') as f:
        n = f.write(lines)
        print(n, 'bytes written')
        n = f.write(short)
        print(n, 'bytes written')
        n = f.write(lines)
        print(n, 'bytes written')
        f.close()
        
    with open(fn,'r') as f:
        result1 = f.read()
        print(len(result1), 'bytes read')
        f.close
        
    fn = '/sd/rats1.txt'
    print()
    print('Single block read/write')
    with open(fn,'w') as f:
        n = f.write(short) # one block
        print(n, 'bytes written')

    with open(fn,'r') as f:
        result2 = f.read()
        print(len(result2), 'bytes read')

    os.umount('/sd')

    print()
    print('Verifying data read back')
    success = True
    if result1 == ''.join((lines, short, lines)):
        print('Large file Pass')
    else:
        print('Large file Fail')
        success = False
    if result2 == short:
        print('Small file Pass')
    else:
        print('Small file Fail')
        success = False
    print()
    print('Tests', 'passed' if success else 'failed')

print("Running SD card test")
sdtest()
