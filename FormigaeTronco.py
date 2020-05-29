N = int(input("Digite a quantidade de formigas a serem colocadas em cima do Tronco: "))
L = float(input("Digite o comprimento do Tronco: "))
x1 = 0
Di1 = 0
tempo = 0
A = 1
k = str(1)


def posição_inicial_formiga(x1, Di1, k):
    x1 = float(input("Digite a posição inicial no eixo X da formiga no tronco: "))
    Di1 = float(input("Digite a Direção que a formiga está olhando: 1 - Direita; ou 2 - Esquerda"))
    if Di1 == 1:
        posição = print("A formiga",A ,"está em",x1 ," no eixo X e olhando para a Direita")
        return posição
    else:
        posição = print("A formiga",A ,"está em",x1 ," no eixo X e olhando para a Esquerda") 
        return posição

 
while A <= N:
    posição_inicial_formiga(x1, Di1, k)
    A = A + 1
    
