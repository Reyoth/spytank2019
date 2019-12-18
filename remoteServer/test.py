import random
import sys
from threading import Thread
import time
import spytank

class detecteur(Thread):


    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        while True :
            dist = spytank.litDistance()
            stop = False
            if dist < 25 :
                spytank.stop()
                spytank.led(0,1)
                spytank.led(1,1)
                spytank.led(2,1)
                spytank.led(3,1)
                stop = True
            else :
                spytank.led(0,0)
                spytank.led(1,0)
                spytank.led(2,0)
                spytank.led(3,0)
            
            return stop
