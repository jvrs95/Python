n = int(input("Digite um número: "))
lista = list()
a = list()
while n != 0:
    lista.append(n)
    n = int(input("Digite um número: "))

for i in range(len(lista)-1, -1, (-1)):
    print(lista[i])

