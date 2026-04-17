
def novo_d(d):
    d_invertido = dict()

    for chave, valor in d.items():
        d_invertido[valor] = chave

    return d_invertido

d = {'a': 1, 'b': 2, 'c': 3}
print("Dicionário invertido: ", novo_d(d))
