import socket
from typing import Type

count = 0

with open("lista.txt", "r") as f:
    lista = [line.strip() for line in f if line.strip()]
    lista.sort()
    for url in lista:
        if ".com" in url:
            count += 1
            try:
                with open("resultado.txt","a") as arquivo:
                    arquivo.write(url+": " + socket.gethostbyname(url) + "\n")
                    #print(url+": " + socket.gethostbyname(url))
            except socket.gaierror:
                pass

print("Total de {} urls encontradas!!".format(count))
