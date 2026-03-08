
# Exercício 3: Tipo de pedido

import json


tipo_valor = input("Informe a chave e o valor: ") 
tipo_valor = json.loads(tipo_valor.replace("'", '"'))
tipo = tipo_valor["tipo"]
valor = tipo_valor["valor"]
match tipo:
    case "venda":
        print(f"{tipo.capitalize()} de {valor}€")
    case "compra":
        print(f"{tipo.capitalize()} de {valor}€")
    case _:
        print("Pedido desconhecido")
