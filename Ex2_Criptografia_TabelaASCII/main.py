
def calcular_chave(chave):
    if not chave:
        raise ValueError("A chave não pode ser vazia.")
    
    soma = 0
    for c in chave:
        soma += ord(c)
    
    return soma


def criptografar(mensagem, chave):
    valor_chave = calcular_chave(chave)
    resultado = []
    
    for c in mensagem:
        codigo = ord(c)
        
        # aplicar deslocamento com rotação (ASCII 32–126)
        novo = ((codigo - 32 + valor_chave) % 95) + 32
        
        resultado.append(novo)
    
    return resultado


def descriptografar(codigos, chave):
    valor_chave = calcular_chave(chave)
    resultado = ""
    
    for codigo in codigos:
        # reverter deslocamento com rotação
        original = ((codigo - 32 - valor_chave) % 95) + 32
        
        resultado += chr(original)
    
    return resultado


def listar(codigos):
    for i, codigo in enumerate(codigos):
        print(f"{i}: {codigo}")


mensagem = "Olá Mundo"
chave = "chave"

codificada = criptografar(mensagem, chave)
print("Criptografado:", codificada)

texto_original = descriptografar(codificada, chave)
print("Descriptografado:", texto_original)
