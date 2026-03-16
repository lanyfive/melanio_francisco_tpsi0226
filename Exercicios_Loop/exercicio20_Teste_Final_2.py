# Exercício Teste Final: Elabore uma base de dados de clientes de uma fábrica de materiais. 
# O programa deverá possibilitar inserção e listagem dos clientes bem como as compras 
# por eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). 
# Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%, 
# se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%. O programa deve 
# validar todas as entradas e na listagem deve parar cliente a cliente e ser possível 
# busca direta por número de cliente.

client = dict()
list_clients = []

while True:
    print("\n===== MENU ====")
    print("1. Inserir Cliente")
    print("2. Listar Clientes")
    print("3. Buscar por Número de Cliente")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        while True:
            num_cli = len(list_clients) + 1
            nom_cli = input("Informe o Nome: ")
            morada = input("Informe a Morada: ")
            tel = input("Informe o Telefone: ")
            nif = input("Informe o NIF: ")
            compra = float(input("Informe o Valor da Compra: "))

            if compra < 100.00:
                desconto = 0.0
            elif(compra >= 100.00 and compra <= 200.00):
                desconto = 0.05
            elif(compra > 200.00 and compra <= 500.00):
                desconto = 0.1
            else:
                desconto = 0.15

            div_fin = compra - (compra * desconto)

            client = { "num_cli" : num_cli, "nom_cli" : nom_cli, "morada" : morada, "tel" : tel, "nif" : nif, "compra" : compra, "div_fin" : div_fin }
                
            list_clients.append(client)

            print(f"\nCliente {nom_cli}, com o Número -> {num_cli} inserido com sucesso!")
            new_yes_no = input("\n\nDeseja inserir novo cliente? S/N: ")
            if new_yes_no.lower() == "n": break
    elif opcao == "2":
        i = 0
        while i <= len(list_clients) - 1:
            client = dict(list_clients[i])
            print(f"\nNúmero de Cliente: {client['num_cli']}")
            print(f"Nome: {client['nom_cli']}")
            print(f"Morada: {client['morada']}")
            print(f"Telefone: {client['tel']}")
            print(f"NIF: {client['nif']}")
            print(f"Valor da Compra: {client['compra']}")
            print(f"Divida Final: {client['div_fin']}")
            opcao = input("Deseja visualizar o próximo cliente? (S/N): ")
            if opcao.lower() != "s":
                break
            i += 1

    elif opcao == "3":
        num_cli_input = int(input("Intruduza o Número de Cliente: "))
        for cliente in list_clients:
            if cliente["num_cli"] == num_cli_input:
                print(f"\nNúmero de Cliente: {cliente['num_cli']}")
                print(f"Nome: {cliente['nom_cli']}")
                print(f"Morada: {cliente['morada']}")
                print(f"Telefone: {cliente['tel']}")
                print(f"NIF: {cliente['nif']}")
                print(f"Valor da Compra: {cliente['compra']}")
                print(f"Divida Final: {cliente['div_fin']}")
                break
        else:
            print("\nCliente não encontrado!\n")
    elif opcao == "4":
        print("\n\nMuito Obrigado!\n\n")
        break
    else:
        print("Opção inválida, tente novamente.")
