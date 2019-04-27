import machine, sdcard, os

SPI_CS = 15
class SD:
    def __init__(self):
        self.spi = machine.SPI(1)
        spi.init()
        sd = sdcard.SDCard(spi,machine(SPI_CS))
    def mount(self,root):
        try:
            os.mount(sd,root)
        except:
            print("Error when attempting to mount the file system")
    def umount(self,root):
        os.umount(root)
        
