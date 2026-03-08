
# Exercício 2: Classificação de nota

nota = float(input("Informe a nota: "))

match nota:
    case n if 0 <= n < 50:
        print("Insuficiente")
    case n if 50 <= n < 70:
        print("Suficiente")
    case n if 70 <= n < 90:
        print("Bom")
    case n if 90 <= n <= 100:
        print("Excelente")
    case _:
        print("Intervalo inválido ou não definido")
