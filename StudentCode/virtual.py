from logger import *
import random

class gpio:
    IN = "input"
    OUT ="output"
    def setup(self, num, direction):
        try:
            log("Setup pin %i for %s" % (num, direction))
        except Exception as err:
            log("Error: %s" % err)
            
def readadc(*arguments):
    return random.random() * 10 + arguments[0] * 10 + 10
    
GPIO = gpio()
