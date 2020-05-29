n = int(input("Digite o valor de n:"))

resto = n % 10
digitosrestantes = n // 10
somadosdigitos = 0
ultimodigito = 0

while digitosrestantes > 0:
    ultimodigito = digitosrestantes % 10
    somadosdigitos = somadosdigitos + ultimodigito
    digitosrestantes = digitosrestantes // 10

soma = resto + somadosdigitos + digitosrestantes

print(soma)
