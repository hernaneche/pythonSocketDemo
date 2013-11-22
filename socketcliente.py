#!/usr/bin/env python
#coding: latin-1
#
#Demostración Cliente Socket
#
#Hernán Eche
#

import socket
import time
import sys

BUFFER_SIZE = 1024    

def printAnswer(clientSock):
    print "Recibe respuesta.."
    data = clientSock.recv(BUFFER_SIZE)
    print "Dato Recibido:", data
    if len(data)==0:
        print "no responde!"
    
def espera(segundos):
    print "Espera "+str(segundos)+ " s.."
    time.sleep(segundos)  
    
def main():
    print "Iniciando cliente python.."
    TCP_IP = 'localhost'
    TCP_PORT = 1235                    
    #AF_INET socket para una familia de direcciones de "internet"
    #SOCK_STREAM ES PARA TCP
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Otras familias por ejemplo son AF_INET6 para ipv6, AF_UNIX para unix socket,
    #IPX(Protocolo Novell para SO NetWare), protocolos inalámbricos,
    #infrarrojo AF_IRDA o de radio AF_BLUETOOTH, etc..
    #En cuanto a la conexión podría ser UDP, poniendo socket.SOCK_DGRAM
    print "Conecta.."    
    clientSock.connect( (TCP_IP, TCP_PORT) ) #Aquí el argumento es una TUPLA
    espera(1)
    printAnswer(clientSock)
    while True:        
        mensaje=raw_input("Ingresar Dato:");
        clientSock.send(mensaje.decode(sys.stdin.encoding).encode('utf-8'))                        
        espera(1)
        printAnswer(clientSock)
    clientSock.close()
        

if __name__ == "__main__":
    main()
