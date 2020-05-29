def Lista_Primos_Não_Primos_até_n(n):
    lista_primos = list()
    lista_não_primos = list()
    if n <=1:
        while n < 1:
            print("número inválido")
            n = int(input("Digite um número natural maior que 0 para saber a lista de primos e não primos até o número digitado: "))
        lista_primos.append(1)
        return(print(lista_primos))
    else:
        a = 2
        k = 1
        while k <= n:
            while a <= k//2:
                if k % a != 0:
                    a = a + 1
                else:
                    lista_não_primos.append(k)
                    break
            if a > k//2:   
                lista_primos.append(k)
                k = k + 1
                a = 2
            else:
                k = k + 1
                a = 2
    soma_primos = len(lista_primos)
    soma_não_primos = len(lista_não_primos)
    Divisão_primos_x_não_primos = soma_primos/soma_não_primos
    return(print("Os números não primos são", lista_não_primos,"com ", soma_não_primos,"itens e os primos são", lista_primos,"com ",soma_primos,"itens, totalizando na Razão (primos / não primos) de", Divisão_primos_x_não_primos))
    
Lista_Primos_Não_Primos_até_n(int(input("Digite um número natural maior que 0 para saber a lista de primos e não primos até o número digitado: ")))
