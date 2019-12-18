import random
import sys
from threading import Thread
import time
import spytank

class detecteur(Thread):


    def __init__(self,stop):
        Thread.__init__(self)
        self.stop = stop

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        dist = spytank.litDistance()
        if dist < 25 :
            spytank.stop()
            spytank.led(0,1)
            spytank.led(1,1)
            spytank.led(2,1)
            spytank.led(3,1)
            self.stop = True
        else :
            spytank.led(0,0)
            spytank.led(1,0)
            spytank.led(2,0)
            spytank.led(3,0)
            self.stop = False

        print(dist)
        time.sleep(0.5)

