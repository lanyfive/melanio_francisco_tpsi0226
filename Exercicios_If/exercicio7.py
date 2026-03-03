
# Exercício 7: Calcular a Média de Notas com Pesos

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)
resultado = "Aprovado" if media_ponderada >= 6.0 else "Reprovado"

print(f"Média: {media_ponderada:.2f}")
print(f"Resultado: {resultado}")