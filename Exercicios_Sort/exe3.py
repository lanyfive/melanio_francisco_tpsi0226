
def ordenar_letras(palavra):
    lista_letras = list(palavra)
    n = len(lista_letras)

    for i in range(n):
        for j in range(0, n - i - 1):
            if ord(lista_letras[j]) > ord(lista_letras[j + 1]):
                lista_letras[j], lista_letras[j + 1] = lista_letras[j + 1], lista_letras[j]

    return ''.join(lista_letras)

palavras = "algoritmo"
print(ordenar_letras(palavras))
