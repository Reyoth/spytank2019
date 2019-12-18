import network
import click
from gtts import tts
import os


ADDRESS ="192.168.1.209"
PORT=1111

audio = tts.gTTS("initialisation du programme",lang="fr")
audio.save("init.mp3")
os.system("mpg321 init.mp3")

print("z : avancer\nq : gauche\ns : reculer\nd : droite\ne/r : led\na : stop\nc : exit")

audio= tts.gTTS("entre une lettre pour piloter le robot comme dans la description", lang="fr")
audio.save("pilote.mp3")
os.system("mpg321 pilote.mp3")

continuer = True
while continuer:

    socket = network.newClientSocket()
    socket.connect((ADDRESS,PORT))
    
    lettre = click.getchar()
    socket.send(lettre.encode())

    reponse = socket.recv(4096)
    print(reponse)

    if lettre == "c":
        continuer = False
