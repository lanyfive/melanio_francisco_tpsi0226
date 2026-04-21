
def comparar_strings(s1, s2):
    i = 0
    
    while i < len(s1) and i < len(s2):
        if ord(s1[i]) < ord(s2[i]):
            return -1
        elif ord(s1[i]) > ord(s2[i]):
            return 1
        i += 1
    
    # prefixo
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    else:
        return 0
    

def comparar_nomes(n1, n2):
    # separar primeiro nome e apelido
    p1_nome, p1_apelido = n1.split()
    p2_nome, p2_apelido = n2.split()
    
    # comparar primeiro nome
    resultado = comparar_strings(p1_nome, p2_nome)
    
    if resultado != 0:
        return resultado
    
    # desempate: apelido
    return comparar_strings(p1_apelido, p2_apelido)


def ordenar_nomes(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparar_nomes(lista[j], lista[j + 1]) == 1:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista


nomes = ["Pedro Pereira", "Ana Beatriz", "Ana Clara", "Carlos Silva", "Beatriz Souza", "Ana Paula", "Pedro Andrade"]

nomes_ordenados = ordenar_nomes(nomes)

print(nomes_ordenados)

