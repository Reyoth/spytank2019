# coding: utf-8 
import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        #print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))



def newServerSocket():
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return tcpsock

def newClientSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def newThread(sock):
    (clientsocket, (ip, port)) = sock
    return ClientThread(ip, port, clientsocket)
