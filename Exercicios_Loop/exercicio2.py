
# Exercício 2: Ler 10 números, e determinar se o número par e número impar.

for i in range(10):
    num = int(input(f"Informe o {i+1}º número: "))
    if num % 2 == 0:
        print(f"{num} é um número par.")
    else:
        print(f"{num} é um número ímpar.")
