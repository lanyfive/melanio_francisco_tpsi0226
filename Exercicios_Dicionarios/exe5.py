
def numero_de_letras(palavra):
    palavra_dict = {}
    for letra in palavra:
        if letra in palavra_dict: palavra_dict[letra] += 1
        else: palavra_dict[letra] = 1

    return palavra_dict

palavra = input("Introduza uma palavra: ")

print(numero_de_letras(palavra))
