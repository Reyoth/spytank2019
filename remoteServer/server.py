import network
import spytank
import os
import time
ADDRESS="192.168.1.209"
PORT=1111

socket = network.newServerSocket()
socket.bind((ADDRESS,PORT))

continuer = True
while continuer :
    dist = spytank.litDistance()
    print("distance" ,dist)
    time.sleep(1)

    if dist < 10 :
        spytank.stop()
        spytank.led(0,1)
        spytank.led(1,1)
        spytank.led(2,1)
        spytank.led(3,1)
        #beep
        print("beep")
        #os.system("mpg321 beep.wav")
        time.sleep(1)

    else :
        spytank.led(0,0)
        spytank.led(1,0)
        spytank.led(2,0)
        spytank.led(3,0)

        socket.listen(10)
        print("en ecoute...")

        thread = network.newThread(socket.accept())
        thread.start()

        #notre communication

        lettre = thread.clientsocket.recv(4096)
        lettre = lettre.decode("utf-8")
        print("message recu : ", lettre)

        vitesse = 255

        if lettre == "z":
            spytank.avance(vitesse)
        elif lettre == "q":
            spytank.gauche(vitesse)
        elif lettre == "s":
            spytank.recule(vitesse)
        elif lettre == "d":
            spytank.droite(vitesse)
        elif lettre == "e":
            spytank.led(0,1)
            spytank.led(1,1)
            spytank.led(2,1)
            spytank.led(3,1)
        elif lettre == "r":
            spytank.led(0,0)
            spytank.led(1,0)
            spytank.led(2,0)
            spytank.led(3,0)
        elif lettre == "a":
            spytank.stop()

        elif lettre == "c":
            spytank.stop()
            continuer = False
        
        thread.clientsocket.send("j'ai bien recu le message".encode())
        

