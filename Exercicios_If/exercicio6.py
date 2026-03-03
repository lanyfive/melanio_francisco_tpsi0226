
# Exercício 6: Desconto de Compra

nome = input("Digite o nome do cliente: ")
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra < 200:
    desconto = valor_compra * 0.10  
elif valor_compra < 500:
    desconto = valor_compra * 0.15
else:
    desconto = valor_compra * 0.20

valor_final = valor_compra - desconto
print(f"Nome: {nome}\nValor da compra: {valor_compra:.2f}€\nDesconto: {desconto:.2f}€\nTotal a pagar: {valor_final:.2f}€")
