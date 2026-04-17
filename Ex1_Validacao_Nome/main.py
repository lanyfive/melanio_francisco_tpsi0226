
def is_valid(name):

    # Nome vazio
    if not len(name):
        return False

    # Primeiro caracter letra maiúscula
    if not (65 <= ord(name[0]) <= 90):
        return False
 
    # Maiuscula meio dos nomes
    names = name.split()
    for element in names:
        for k in range(len(element)):
            if (65 <= ord(element[k]) <= 90) and k > 0:
                return False

    # Apenas letras e espaços
    for i in range(len(name)):
        c = name[i]
        if not ((65 <= ord(c) <= 90) or (97 <= ord(c) <= 122) or c == " "):
            return False

        # Espaço encontrado
        if c == " ":
            # Espaço no fim do nome
            if i == len(name) - 1:
                return False

            # Maiuscula depois do Espaço
            next_c = name[i + 1]            
            if not (65 <= ord(next_c) <= 90):
                return False

    return True


full_name = input("Digite seu nome completo: ")

if is_valid(full_name):
    print("Nome válido!")
else:
    print("Nome inválido: contém caracteres não permitidos.")
