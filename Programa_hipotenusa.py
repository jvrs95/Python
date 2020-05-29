def soma_hipotenusas(n):
    print ("As hipotenusas são")
    soma_hipotenusas = 0
    a = 1
    b = 1
    while n > 1:
        while b < n:
            while n**2 != a**2 + b**2 and a < n:
                a = a + 1
            if n**2 == a**2 + b**2:
                soma_hipotenusas = soma_hipotenusas + n            
                b = b + 1
                a = 1                
                print (n, end = " ")
                n = n - 1
            else:
                b = b + 1
                a = 1
        n = n - 1
        b = 1
    print()
    print("O Valor da Soma das Hipotenusas é")
    return (soma_hipotenusas)

print(soma_hipotenusas(int(input("digite o valor de h:"))))

