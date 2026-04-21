
def comparar_palavras(p1, p2):
    i = 0
    
    while i < len(p1) and i < len(p2):
        c1 = ord(p1[i])
        c2 = ord(p2[i])
        
        if c1 < c2:
            return -1  # p1 vem antes
        elif c1 > c2:
            return 1   # p2 vem antes
        
        i += 1
    
    # palavras com o mesmo prefixo
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


palavras = ["banana", "uva", "abacaxi", "laranja"]
resultado = ordenar_lista(palavras)

print(resultado)