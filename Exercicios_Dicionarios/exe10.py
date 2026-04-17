
def numero_de_palavras(frase):
    frase_dict = {}
    for palavra in frase.lower().split():
        if palavra in frase_dict: frase_dict[palavra] += 1
        else: frase_dict[palavra] = 1

    return frase_dict

frase = input("Introduza uma frase: ")

print(numero_de_palavras(frase))
