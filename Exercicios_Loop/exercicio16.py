
# Exercício 16: Calcula a média de 30 números pares. Valida a entrada de números inteiros entre 1 e 50.

sum = 0
for i in range(1, 31):
    num = -1
    while num < 1 or num > 50 or num % 2 != 0:
        num = int(input(f"Introduza o {i}º número (Deve ser PAR e estar entre 1 e 50): "))
    sum += num

print(f"Média = {(sum / 30):.2f}")
