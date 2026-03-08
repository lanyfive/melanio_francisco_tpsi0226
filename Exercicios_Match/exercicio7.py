
# Exercício 7: Classificação de produto

produto = eval(input("Digite as informações do produto: "))

match produto:
    case {"categoria": "eletrônico", "preco": preco} if preco > 1000:
        print("Produto de luxo")
    case {"categoria": "eletrônico", "preco": preco} if preco <= 1000:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")
