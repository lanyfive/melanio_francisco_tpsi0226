
def total_vendas():
    soma = 0
    for valor in vendas.values():
        soma += valor

    return soma

vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}
print("Total de Vendas: ", total_vendas())
