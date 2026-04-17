
produto = {}

def create_produto():
    global produto
    
    produto = {
        "nome": "Telemóvel",
        "preco": 1500,
        "stock": 30
    }

def remove_key(produto, chave):
    produto.pop(chave)


create_produto()
remove_key(produto, "stock")
print(produto)
