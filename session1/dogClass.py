#!/usr/bin/env python3
# a demo program demonstrating a Python class
class Dog():
# initialize the class- This is called when gthe class is created
    def __init__(self,name):
        self.name = name
    
    def sit(self):
        self.sit = True
        
    def run(self):
        self.sit = False
        
    def action(self):
        if self.sit:
            return("is sitting")
        else:
            return("is running")
        
if __name__ == '__main__':
    # create a dog object
    myDog = Dog('Bingo')
    print('Making Bingo sit!')
    myDog.sit()
    print(myDog.name+' '+myDog.action())
    print('Releasing Bingo')
    myDog.run()
    print(myDog.name+' '+myDog.action())    
    
          
                
            
        
        