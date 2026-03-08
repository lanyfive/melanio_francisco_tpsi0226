
# Exercício 8: Operação matemática
operacao = input("Informe a operação (soma, subtrai, multiplica, divide): ")
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

match operacao:
    case "soma":
        resultado = num1 + num2
    case "subtrai":
        resultado = num1 - num2
    case "multiplica":
        resultado = num1 * num2
    case "divide":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero"
    case _:
        resultado = "Operação inválida"

print(f"Resultado: {resultado}")
