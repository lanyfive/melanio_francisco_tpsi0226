
# Exercício 9: Solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100. (Use o ciclo do ... while)

num = 0
while num < 1 or num > 100:
    num = int(input("Informe um número (entre 1 e 100): "))

print(f"O número introduzido é: {num}")
