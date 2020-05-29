n = 1

while n > 0:
    n = int(input("Digite um número natural:"))
    fatorial = 1
    if n < 0:
        print ("O número digitado não é um número natural!")
    else:
        while n >= 1:
            fatorial = n*fatorial
            n = n - 1
        print (fatorial)
