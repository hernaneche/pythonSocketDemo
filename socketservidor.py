#!/usr/bin/env python
#coding: latin-1
#
#Demostración Server Socket (sin threads)
#
#Hernán Eche
#
 
import socket
import sys

def main():
    host = 'localhost'
    port = 1235

    buffer_size = 1

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSock.bind((host, port))
    serverSock.listen(1)
    try:
      while True:
          print "\n\nPython Espera Conexiones en..."+ str(port)
          clientSock, address = serverSock.accept() #Devuelve una tupla
          print "Cliente conectado: " + str(address)
          clientSock.send("Hola desde PythonServer!")        
          while True:
                data = clientSock.recv(buffer_size)
                if not data or data=='q':
                    break
                sys.stdout.write(data.decode('utf-8'))
                clientSock.send(data.encode('utf-8')) #eco reenvia todo lo que recibe, salvo que reciba una q
          clientSock.send("Adiós desde PythonServer!")        
          clientSock.close()
          print "\nCliente desconectado:" + str(address)
    finally:    
        serverSock.close()

if __name__ == "__main__":
    main()
