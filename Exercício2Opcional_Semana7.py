def soma_hipotenusas(n):
    a = 1
    b = 1
    h = 2
    while h < n:
        a = 1
        while a < h:
            b = 1
            while h**2 != a**2 + b**2:
                b = b + 1
                if b == h:
                    break
                else: print(h)
            a = a + 1
            if a == h:
                break    
        h = h + 1
    print(h)
soma_hipotenusas(int(input("Digite o valor de n:")))
    
