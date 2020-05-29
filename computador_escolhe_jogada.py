def computador_escolhe_jogada(n, m):
    if n <= 0 or m < 1:
        return("opção inválida")
    else:
        if n <= m:
            return n
        else:
            resto = n % (m + 1)
            if resto == 0:
                return m
            else:
                if resto > m:
                    return m
                else:
                    return resto


        
