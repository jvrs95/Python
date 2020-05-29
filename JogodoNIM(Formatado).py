m = 0
n = 0
computador = 0
jogador = 0

def partida():
    k = 0
    n = int(input("Quantas peças? "))
    while n <= 0:
        print("A quantidade de peças informada é inválida! Por favor indique um número inteiro positivo maior que 0")
        n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m <= 0:
        print("O limite de peças por jogada informado é inválido! Por favor indique um número inteiro positivo maior que 0")
        m = int(input("Quantas peças? "))
    if n <= m:
        print("Computador começa!")
        n = n - computador_escolhe_jogada(n, m)
        if n == 0:
            print("Fim do Jogo, o computador ganhou!")
        else:
            print("Fim do Jogo, Você ganhou!")
    else:     
        if n % (m + 1) == 0:
            print("Você começa!")
            print()
            while n > 0:
                n = n - usuario_escolhe_jogada (n, m)
                if n == 0:
                    k = 15
                else:
                    n = n - computador_escolhe_jogada (n, m)
            if k == 15:
                print("Fim do Jogo, você ganhou!")
            else:
                print("Fim do Jogo, o computador ganhou!")
                           
        else:
            print("Computador começa!")
            while n > 0:
                n = n - computador_escolhe_jogada(n, m)               
                if n == 0:
                    k = 15
                else:
                    n = n - usuario_escolhe_jogada(n, m)
            if k == 15:
                print("Fim do Jogo, o computador ganhou!")
            else:
                print("Fim do Jogo, Você ganhou!")
                   
        
def campeonato():
    k = 0
    r = 1
    voce = 0
    computador = 0
    while computador < 3 and voce < 3:
        k = 0
        print("**** Rodada", r, "****")
        print()
        n = int(input("Quantas peças? "))
        while n <= 0:
            print("A quantidade de peças informada é inválida! Por favor indique um número inteiro positivo maior que 0")
            n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        while m <= 0:
            print("O limite de peças por jogada informado é inválido! Por favor indique um número inteiro positivo maior que 0")
            m = int(input("Quantas peças? "))
        if n <= m:
            print("Computador começa!")
            n = n - computador_escolhe_jogada(n, m)
            if n == 0:
                print("Fim do Jogo, o computador ganhou!")
                computador = computador + 1
                r = r + 1
            else:
                print("Fim do Jogo, Você ganhou!")
                voce = voce + 1
                r = r + 1
        else:     
            if n % (m + 1) == 0:
                print("Você começa!")
                print()
                while n > 0:
                    n = n - usuario_escolhe_jogada (n, m)
                    if n == 0:
                        k = 15
                    else:
                        n = n - computador_escolhe_jogada (n, m)
                if k == 15:
                    print("Fim do Jogo, você ganhou!")
                    voce = voce + 1
                    r = r + 1
                else:
                    print("Fim do Jogo, o computador ganhou!")
                    computador = computador + 1
                    r = r + 1
                           
            else:
                print("Computador começa!")
                while n > 0:
                    n = n - computador_escolhe_jogada(n, m)               
                    if n == 0:
                        k = 15
                    else:
                        n = n - usuario_escolhe_jogada(n, m)
                if k == 15:
                    print("Fim do Jogo, o computador ganhou!")
                    computador = computador + 1
                    r = r + 1
                else:
                    print("Fim do Jogo, Você ganhou!")
                    voce = voce + 1
                    r = r + 1
            
    print("Placar: Você", voce," X", computador," Computador")
             
def inicio():
    pc = 5
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada") 
    pc = int(input("2 - para jogar um campeonato "))
    while pc != 1 and pc != 2:
        print("opção inválida!")
        print("1 - para jogar uma partida isolada") 
        pc = int(input("2 - para jogar um campeonato "))

    if pc == 1:
        print()
        print("Você escolheu uma partida isolada!")
        partida()

    else:
        print()
        print("Voce escolheu um campeonato!")
        print()
        campeonato()

def usuario_escolhe_jogada(n, m):
    if n < 0 or m < 1:
        return("opção inválida")
    if n == 0:
        return n
    else:
        usuario = 0
        usuario = int(input("Quantas peças você vai tirar? "))
        print()
        while usuario > m or usuario <= 0 or usuario > n:
            print("oops! Jogada inválida! Tente de novo.")
            print()
            usuario = int(input("Quantas peças você vai tirar? "))
            print()
        print("Você tirou", usuario,"peças.")
        n = n - usuario
        if n > 0:
            print("Agora restam",n ,"peças no tabuleiro.")            
            return usuario
        else:
            return usuario
           
def computador_escolhe_jogada(n, m):
    if n <= 0 or m < 1:
        return("opção inválida")
    else:
        if n <= m:
            print("O computador tirou", n,"peças.")
            return n
        else:
            resto = n % (m + 1)
            if resto == 0:
                print("O computador tirou", m,"peças.")
                return m
            else:
                if resto > m:
                    print("O computador tirou", m,"peças.")
                    n = n - m
                    print("Agora restam",n,"peças no tabuleiro.")
                    return m
                else:
                    print("O computador tirou", resto,"peças.")
                    n = n - resto
                    print("Agora restam",n ,"peças no tabuleiro.")
                    return resto

     
inicio()
