
# Exercício 4: Leia um número inteiro, e diga se ele é um número primo ou não.

num = int(input("Introduza o número: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")
else:
    print("O Número deve ser maior que 1.")
