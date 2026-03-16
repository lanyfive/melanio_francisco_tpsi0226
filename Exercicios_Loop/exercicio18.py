# Exercícios 18: Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. 
# Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial. 6=3+2+1 .

num = int(input("Introduza um número: "))

i = 0
for j in range(1, num + 1):
    soma = 0
    for k in range(1, j):
        if j % k == 0:
            soma += k
    if soma == j:
        i += 1

print(f"Quantidade de Números Perfeitos até {num}: ", i)
