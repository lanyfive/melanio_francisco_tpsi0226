
# Exercício 10: Lê um número e escreve quantos divisores ele possui.

num = int(input("Introduza um número: "))
divisors = 0

for i in range(1, num + 1):
    if num % i == 0: divisors += 1

print(f"{num} possui {divisors} divisores.")
