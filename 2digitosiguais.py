a = int(input("Digite um número: "))

restante_prim = 11
resto_seg = 1
resto_prim = 2

while restante_prim>= 10 and resto_seg != resto_prim:
    resto_prim = a % 10
    restante_prim = a // 10
    resto_seg = restante_prim % 10
    a = a // 10

if resto_seg == resto_prim and a != 0:
    print("sim")
    
else:
    print("não")

