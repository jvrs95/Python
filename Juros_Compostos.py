def juros_compostos():
    lista = list()
    x = int(input("Digite o Capital Inicial a ser investido: "))
    taxa_mensal = float(input("Digite a Taxa Mensal de Juros: "))
    Montante_posterior = x
    n = 1
    while n <=12:
        Montante_posterior = Montante_posterior + Montante_posterior*taxa_mensal
        n = n + 1
    taxa_anual = Montante_posterior/x
    variação_taxas = taxa_anual/taxa_mensal
    lista.append(taxa_anual)
    lista.append(variação_taxas)
    return (lista)


def calculo_taxa_mensal():
    a = juros_compostos()
    taxa_mensal = a[0]/ a[1]
    
calculo_taxa_mensal()
