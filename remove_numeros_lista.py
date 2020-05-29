def remove_numeros(lista):
    b = list()
    a = list(lista)
    for i in range(len(a)):
        if a[i] != '0' and a[i] != '1' and a[i] != '2' and a[i] != '3' and a[i] != '4' and a[i] != '5' and a[i] != '6' and a[i] != '7' and a[i] != '8' and a[i] != '9' and a[i] != ',' and a[i] != '[' and a[i] != ']':
            b.append(a[i])
    return (b)
