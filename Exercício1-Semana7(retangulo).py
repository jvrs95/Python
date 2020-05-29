largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
l = 1

while altura > 0:
    l = 1
    while l < largura:
        print("#", end = "")
        l = l + 1
    print("#")
    altura = altura - 1
    
