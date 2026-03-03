
# Exercício 5: Ler 3 Valores e Exibir em Ordem Crescente e Decrescente

val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
val3 = int(input("Digite o terceiro valor: "))
if val1 == val2 == val3:
    print("Os três valores são iguais.")
elif val1 >= val2 and val2 >= val3:
    print(f"Crescente: {val3}, {val2}, {val1}")
    print(f"Decrescente: {val1}, {val2}, {val3}")
elif val1 >= val3 and val3 >= val2:
    print(f"Crescente: {val2}, {val3}, {val1}")
    print(f"Decrescente: {val1}, {val3}, {val2}")
elif val2 >= val1 and val1 >= val3:
    print(f"Crescente: {val3}, {val1}, {val2}")
    print(f"Decrescente: {val2}, {val1}, {val3}")
elif val2 >= val3 and val3 >= val1:
    print(f"Crescente: {val1}, {val3}, {val2}")
    print(f"Decrescente: {val2}, {val3}, {val1}")
elif val3 >= val1 and val1 >= val2:
    print(f"Crescente: {val2}, {val1}, {val3}")
    print(f"Decrescente: {val3}, {val1}, {val2}")
else:
    print(f"Crescente: {val1}, {val2}, {val3}")
    print(f"Decrescente: {val3}, {val2}, {val1}")
