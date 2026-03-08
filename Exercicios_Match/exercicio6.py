
# Exercício 6: Estado do Servidor

info_servidor = eval(input("Digite as informações do servidor: "))

match info_servidor:
    case {"status": "ok"}:
        print("Servidor ativo")
    case {"status": "ok", "tempo_resposta": tempo} if tempo > 200:
        print("Servidor lento")
    case {"status": "error"}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")
