def melhor_de_três():
    a = input("1º Jogador: ")
    b = input("2º Jogador: ")
    vitorias_a = 0
    vitorias_b = 0
    while vitorias_a < 3 and vitorias_b < 3:
        ganhador = input("Quem ganhou a partida? ")
        if ganhador == a:
            vitorias_a = vitorias_a + 1
        if ganhador == b:
            vitorias_b = vitorias_b + 1
    return(print("Jogo acabou!",a, vitorias_a,"x", vitorias_b, b))

def melhor_de_cinco():
    a = input("1º Jogador: ")
    b = input("2º Jogador: ")
    vitorias_a = 0
    vitorias_b = 0
    while vitorias_a < 5 and vitorias_b < 5:
        ganhador = input("Quem ganhou a partida? ")
        if ganhador == a:
            vitorias_a = vitorias_a + 1
        if ganhador == b:
            vitorias_b = vitorias_b + 1
    return(print("Jogo acabou!",a, vitorias_a,"x", vitorias_b, b))

def inicia_campeonato():
    lista_de_participantes = list()
    n = 1
    quantidade_participantes = int(input("Digite a quantidade de participantes"))
    while n < quantidade_participantes:
        lista_de_participantes.append(input("Digite o nome do participante"))
        n = n + 1
    return(print(lista_de_participantes))


