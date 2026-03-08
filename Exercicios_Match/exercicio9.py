
# Exercício 9: Processamento de requisição

requisicao = eval(input("Digite as informações da requisição: "))

match requisicao:
    case {"metodo": "GET"}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": conteudo} if conteudo:
        print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": conteudo} if not conteudo:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")
