
def comparar_palavras(p1, p2):
    i = 0
    while i < len(p1) and i < len(p2):
        if ord(p1[i]) < ord(p2[i]):
            return -1
        elif ord(p1[i]) > ord(p2[i]):
            return 1
        i += 1
    
    # prefixo
    if len(p1) < len(p2):
        return -1
    elif len(p1) > len(p2):
        return 1
    else:
        return 0


def ordenar_lista(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparar_palavras(lista[j], lista[j + 1]) == 1:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista


def agrupar_e_ordenar(lista):
    grupos = {}
    
    # Agrupar
    for palavra in lista:
        inicial = palavra[0].lower()  # normalizar
        
        if inicial not in grupos:
            grupos[inicial] = []
        
        grupos[inicial].append(palavra)
    
    # Ordenar cada grupo
    for chave in grupos:
        grupos[chave] = ordenar_lista(grupos[chave])
    
    return grupos


palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
palavras_ordenadas = agrupar_e_ordenar(palavras)

print(palavras_ordenadas)
