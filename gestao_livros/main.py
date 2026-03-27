# GESTÃO DE LIVROS

livros = []

while True:
    print("\n===== MENU ====")
    print("1. Adicionar novo livro")
    print("2. Procurar por título ou autor")
    print("3. Excluir livro")
    print("4. Ordenar livros")
    print("5. Listar livros")
    print("6. Sair")
    opcao_menu = int(input("Escolha uma opção (1-6): "))

    match(opcao_menu):
        case 1:
            print("\n=== ADICIONAR LIVRO")
            while True:
                if len(livros) == 100:
                    print("Atingiu o máximo de 100 livros cadastrados. Já não pode adicionar livros.")
                    break

                codigo = "00" + str(len(livros) + 1)
                titulo = input("Título: ")
                autor = input("Autor: ")
                ano = input("Ano de publicação: ")

                novo_livro = { "codigo" : codigo, "titulo" : titulo, "autor" : autor, "ano" : ano }
                livros.append(novo_livro)

                print(f"\nLivro com o Código->{codigo} criado com sucesso!")            
                continuar = input("Deseja continuar a adicionar livros? Responda com 'S' ou 'N': ")
                if continuar.lower() == "n": break
        case 2:
            print("\n=== PROCURAR LIVRO")
            print("1. Procurar por título")
            print("2. Procurar por autor")
            print("3. Sair")
            opcao_procurar = int(input("Escolha um critério de busca: "))
            match(opcao_procurar):
                case 1:
                    print("\n=== PROCURAR LIVRO POR TÍTULO")
                    procurar_titulo = input("Intruduza o Título do Livro: ")
                    for livro in livros:
                        if livro["titulo"] == procurar_titulo:
                            print(f"\n{livro['titulo']} - {livro['autor'].upper()}, {livro['ano']}")
                            break
                    else:
                        print("\nLivro não encontrado!\n")
                case 2:
                    print("\n=== PROCURAR LIVRO POR AUTOR")                    
                    procurar_autor = input("Intruduza o Autor do Livro: ")
                    for livro in livros:
                        if livro["autor"] == procurar_autor:
                            print(f"\n{livro['titulo']} - {livro['autor'].upper()}, {livro['ano']}")
                            break
                    else:
                        print("\nLivro não encontrado!\n")                    
        case 3:
            print("\n=== EXCLUIR LIVRO")
            excluir_codigo = input("Intruduza o Código do Livro: ")
            for livro in livros:
                if livro["codigo"] == excluir_codigo:
                    index = livros.index(livro)
                    del livros[index]
                    break
            else:
                print("\nLivro não encontrado!\n")
        case 4:
            print("\n=== ORDENAR LIVROS")
            print("\nEsta funcionalidade está em desenvolvimento...")
        case 5:
            print("\n=== LISTAR LIVROS")
            if len(livros) == 0:
                print("Ainda não possui livros cadastrados.")
            else:
                i = 0
                while i <= len(livros) - 1:
                    livro = dict(livros[i])
                    print(f"{livro['titulo']} - {livro['autor'].upper()}, {livro['ano']}")
                    i += 1            
        case 6:
            print("\n=== SAIR")
            print("Muito obrigado!!!")
            break
