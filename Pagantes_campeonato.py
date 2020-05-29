import re

def Quem_Pagou():
    lista_de_inscritos = list()
    lista_de_pagamentos = list()
    lista_de_restos_a_pagar = list()
    lista_de_inscritos_pagamento_restos = list()
    n = 1
    quantidade_inscritos = int(input("Digite a quantidade de inscritos: "))
    valor_inscrição = int(input("Digite o valor da inscrição: "))
    while n <= quantidade_inscritos:
        a = input("Digite o nome do inscrito: ")
        lista_de_inscritos.append(a)
        b = int(input("Digite quanto ele já pagou: "))
        lista_de_pagamentos.append(b)
        c = valor_inscrição - b
        lista_de_restos_a_pagar.append(c)
        d = (a, "já pagou", b, "faltam ", c)
        lista_de_inscritos_pagamento_restos.append(d)
        n = n + 1
    acrescentar = input("Alguém pagou mais alguma coisa recentemente?")
    if acrescentar == "sim":
        quantidade_acrescentar = int(input("Quantos pagaram a mais?"))
        z=1
        while z <= quantidade_acrescentar:
            nome_acrescentar = input("Quem? ")
            for i in range(len(lista_de_inscritos)):
                if lista_de_inscritos[i] == nome_acrescentar:
                    acrescimo_efetuado = int(input("Quanto ele pagou?"))
                    lista_de_pagamentos[i] = lista_de_pagamentos[i] + acrescimo_efetuado
                    lista_de_restos_a_pagar[i] = lista_de_restos_a_pagar[i] - acrescimo_efetuado
            z = z + 1
        final = zip (lista_de_inscritos, lista_de_pagamentos, lista_de_restos_a_pagar)
        for i in list(final):
            print(i)
    else:
        final = zip (lista_de_inscritos, lista_de_pagamentos, lista_de_restos_a_pagar)
        for i in list(final):
            print(i)

Quem_Pagou()
