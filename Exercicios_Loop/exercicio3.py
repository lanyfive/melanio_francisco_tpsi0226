
# Exercício 3: Ler a nota de 10 alunos, calcular a media e mostrar essa média.

sum = 0
for i in range(10):
    score = float(input(f"Informe a nota do {i+1}ª aluno: "))
    sum += score

average = sum / 10
print(f"A média das notas é: {average:.2f}")
