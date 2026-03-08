
# Exercício 5: Análise de mensagem

mensagem = input("Digite uma mensagem: ")

match mensagem.lower():
    case "olá" | "bom dia":
        print("Saudação")
    case _ if mensagem.endswith("?"):
        print("Pergunta")
    case _ if "tchau" in mensagem.lower() or "adeus" in mensagem.lower():
        print("Despedida")
    case _:
        print("Mensagem genérica")
