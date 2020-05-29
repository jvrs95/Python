def sem_sobras():
    a = float(input("Digite o valor total a gastar"))
    b = float(input("Digite o valor inicial da ação"))
    c = float(input("Digite a quantidade inicial da ação"))
    valor_inicial = b
    quantidade_inicial = c
    resto = a % (b*c)
    a = b*c + resto
    while a % (b*c) != 0 and c >= quantidade_inicial - 0.01:
        while a % (b*c) != 0 and b >= valor_inicial -0.01:
            b = b - 0.01
        if a % (b*c) == 0:
            return(print(a, b, c))
        else:
            c = c + 0.01
            b = valor_inicial
    if a % (b*c) == 0:
        return(print(a,b,c))
    else:
        return(print("mesmo com", a, b, c, "não foi possível achar o resultado, então vai ter que sobrar"))
            
sem_sobras()
