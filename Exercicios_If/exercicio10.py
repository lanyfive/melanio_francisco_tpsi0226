
# Exercício Loop: Identificar Números Pares e Ímpares

numeros = []

for i in range(10):
    num = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

par = 0
impar = 0
for numero in numeros:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Pares: {par}\nÍmpares: {impar}")
