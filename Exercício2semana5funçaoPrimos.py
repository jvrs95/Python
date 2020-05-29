def éPrimo(k):
    if k <= 1:
        if k < 0:
            return ("número inválido")
        else:
            if k == 0:
                return ("não existe")
            else:
                if k == 1:
                    return (1)
    else:
        a = 3
        while k % a != 0:
            a = a + 1
        if a < k and a > 1:
            return ("não primo")
        else:
            return ("primo")
    
def maior_primo(n):
    if n < 2:
        return "não existe"
    else:
        if n == 2:
            return (2)
        else:
            if n == 3:
                return(3)
            else:
                if n == 4:
                    return(3)
                else:
                    p = 1
                    k = 3
                    while k < n:
                        if éPrimo(k) == "não primo":
                            k = k + 1
                        else:
                            p = k
                            k = k + 1
                    if éPrimo(n) == "primo":
                        return (n)
                    else:
                        return (p)

