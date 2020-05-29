def remove_repetidos(lista):
    lista_intermediaria = list()
    b = list()
    a = list(lista)
    for i in range(len(a)):
        if a[i] != '[' and a[i] != ']' and a[i] != ',':
            b.append(int(a[i]))
    for i in range(len(b)):
        if i < len(b)+1:
            if b[i] not in b[(i+1):]:
                lista_intermediaria.append(b[i])
    
    lista_final = sorted(lista_intermediaria)
    return print(lista_final)

remove_repetidos(input("Digite sua Lista: "))
