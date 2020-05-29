largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
l = 1
a = altura
while altura > 0:
    l = 1
    while l < largura:
        if altura != a and altura != 1:
            if l == 1:
                print("#", end="")
                l = l + 1
            else:
                print(" ", end = "")
                l = l + 1
        else:
            print("#", end = "")
            l = l + 1
    print("#")
    altura = altura - 1
    
    
