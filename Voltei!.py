import random
v=1
f=list()
k= int(input("Quantos são os subtópicos? "))
while v<=k:
    a=int(input("digite o número da 1 questão do subtópico: "))
    z=int(input("digite o número da última questão do subtópico: "))
    d=list()
    e = random.randrange(a, z)

    while e >= a and e <= z and len(d)<=z-a:
        if e not in d and e>0:
            d.append(e)
            e = random.randrange(a, z+1)
        else:
            e = random.randrange(a,z+1)


    f.append(d)
    v = v+1
    
print (f)

for i in f:
    print(random.randrange(i))



