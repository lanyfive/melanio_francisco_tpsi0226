
# Exercício 3: Mostrar Números em Ordem Crescente e Decrescente

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 == num2:
    print("Os números são iguais.")
elif num1 > num2:
    print(f"Crescente: {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}")
else:
    print(f"Crescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")
