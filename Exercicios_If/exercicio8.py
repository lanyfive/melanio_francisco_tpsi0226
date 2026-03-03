
# Exercício 8: Calcular a Média de 10 Notas e informar notas iguais ou acima da media

notas = []

for i in range(10):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Média: {media:.2f}")

i = 0
for nota in notas:
    if nota >= media:
        i += 1
print(f"Alunos com notas iguais ou acima da média: {i}")