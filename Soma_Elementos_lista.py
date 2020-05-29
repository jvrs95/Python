def soma_elementos(lista):
    b = list()
    a = list(lista)
    for i in range(len(a)):
        if a[i] != '[' and a[i] != ']' and a[i] != ',':
            b.append(int(a[i]))
    Soma = 0
    for i in range(len(b)):
        Soma = Soma + b[i]
    return Soma

soma_elementos(input("Digite sua Lista: "))
