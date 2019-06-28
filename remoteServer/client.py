import network
import click


ADDRESS ="10.0.0."
PORT=1111

print("z : avancer\nq : gauche\ns : reculer\nd : droite\ne/r : led\na : stop\nc : exit")
print("entre une lettre pour piloter le robot comme dans la description")

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
