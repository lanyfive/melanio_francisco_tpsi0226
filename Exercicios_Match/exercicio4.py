
# Exercício 4: Tipo de dado

valor = input("Digite um valor: ")
dado = eval(valor)

match dado:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case str() if not dado.isnumeric():
        print("Texto")
    case str() if dado.isnumeric():
        print("Número em formato de texto")
    case list():
        print("Lista de inteiros")
    case _:
        print("Tipo de dado desconhecido")
