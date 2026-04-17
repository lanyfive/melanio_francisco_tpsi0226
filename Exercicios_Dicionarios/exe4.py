
def exist_key(utilizador):
    for chave in utilizador.keys():
        if chave == "email":
            return True
    return False

utilizador = {'nome': 'Carlos', 'idade': 28}
mensagem = "Chave 'Email' existe." if exist_key(utilizador) else "Email não encontrado."
print(mensagem)
