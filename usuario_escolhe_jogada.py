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
