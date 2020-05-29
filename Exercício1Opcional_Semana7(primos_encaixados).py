p = 0
k = 3
a = 2

def n_primos(n):
    p = 0
    k = 3
    a = 2
    if n < 2:
        return ("número inválido")
    if n == 2:
        return (1)
    else:    
        while k <= n:
            a = 2
            while k % a != 0:
                a = a + 1
            if a < k and k > 1:               
                k = k + 1
            else:               
                k =  k + 1
                p = p + 1
        return (p + 1)

n_primos(int(input("Digite o valor de n:")))
    

    
    
