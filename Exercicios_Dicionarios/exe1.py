
alunos = []

def create(nome, idade, curso):
    aluno = {"nome": nome , "idade": idade, "curso": curso}
    alunos.append(aluno)


while(True):
    print("### Menu ###")
    print("1. Inserir um Aluno")
    print("2. Listar alunos")
    print("3. Sair")
    op = int(input("\nEscolha uma opção no MENU: "))

    match(op):
        case 1:
            while (True):
                nome = input("Informe o nome do aluno: ")
                idade = input("Informe a idade do aluno: ")
                curso = input("Indique o curso: ")

                create(nome, idade, curso)

                continuar = input("\nDeseja continuar a inserir alunos? Responda com 'S' ou 'N' ")
                if continuar.lower() == "n": break
        case 2:
            for aluno in alunos:
                print("Nome: ", aluno["nome"])
                print("Idade: ", aluno["idade"])
                print("Curso: ", aluno["curso"])
        case 3:
            print("\nSAIR...")
            print("Muito obrigado!!!")
            break
        case _:
            print("\nEntrada inválida.")            
            