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
                print(k, "não é primo")
                k = k + 1
            else:
                print(k, "é primo")
                k =  k + 1
                p = p + 1
        print ("Existem",p + 1 ,"números primos até", n)


    

    
    
