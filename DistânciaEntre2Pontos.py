import math

a = int(input("Digite a coordenada X do Ponto A:"))
b = int(input("Digite a coordenada Y do Ponto A:"))
c = int(input("Digite a coordenada X do Ponto B:"))
d = int(input("Digite a coordenada Y do Ponto B:"))

distanciaAB = (c - a) * 2 + (d - b) * 2

if distanciaAB >= 10:
    print("longe")
else:
    print("perto")

    

    
    
