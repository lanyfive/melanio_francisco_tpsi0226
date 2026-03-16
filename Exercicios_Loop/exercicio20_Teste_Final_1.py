# Exercício Teste Final: Elabore um programa que leia um valor de entrada e mostre para cada 
# valor até ao 1 (se é número Primo, Quantos divisores e números perfeitos) o Programa 
# deve validar entradas entre 1 e 30.000, e parar de 10 em 10 valores com instrução para 
# parar ou continuar. No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) 
# com a função extra tabuada. Validar entradas de 1 a 1000 (nota a tabuada deve apresentar 
# todas as multiplicações de 1 ate ao máximo introduzido) deve parar de 20 em 20 valores.

op = -1
while op != 3:
    print("\n===== MENU =====")
    print("1 - Verificar número: Primo, Divisores e Números Perfeitos")
    print("2 - Calculadora simples (+,-,*,/)")
    print("3 - Sair")
    op = int(input("Escolha uma opção (1-3): "))

    if op == 1:
        valor = 0
        while valor < 1 or valor > 30000:
            valor = int(input("Introduza um número (De 1 a 30000): "))
    
        pausa = 0
        for n in range(1, valor + 1):
            divisores = 0
            soma = 0

            for i in range(1, n + 1):
                if n % i == 0:
                    divisores += 1
                    if i != n:
                        soma += i

            print("\nNúmero:", n)
            print("Divisores:", divisores)

            if divisores == 2:
                print("O Número é Primo")
            else:
                print("O Número não é Primo")

            if soma == n and n != 0:
                print("O Número é Perfeito")
            else:
                print("O Número não é Perfeito")

            pausa += 1

            if pausa == 10:
                resp = input("Deseja Continuar? (S/N): ")
                if resp.upper() != "S":
                    break
                pausa = 0
    elif op == 2:
        op2 = -1
        while op2 != 6:
            print("\n===== CALCULADORA =====")
            print("1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Tabuada")
            print("6 - Voltar")
            op2 = int(input("Escolha uma opção (0 - 5): "))

            if op2 >= 1 and op2 <= 4:
                a = float(input("Informe o primeiro número: "))
                b = float(input("Informe o segundo número: "))
                if op2 == 1:
                    print("Soma:", a + b)
                elif op2 == 2:
                    print("Diferença:", a - b)
                elif op2 == 3:
                    print("Produto:", a * b)
                elif op2 == 4:
                    if b == 0:
                        print("Erro divisão por zero")
                    else:
                        print("Quociente:", a / b)

            elif op2 == 5:
                limite = 0
                while limite < 1 or limite > 1000:
                    limite = int(input("Valor máximo (1-1000): "))

                pausa = 0

                for i in range(1, limite + 1):
                    for j in range(1, 11):
                        print(i, "x", j, "=", i * j)
                        pausa += 1
                        if pausa == 20:
                            resp = input("Deseja continuar? (S/N): ")
                            if resp.lower() != "s":
                                break
                            pausa = 0

                    if pausa == 20 and resp.lower() != "s":
                        break
    elif op == 3:
        print("\nMuito obrigado!\n")
    else:
        print("Esta opção de MENU é inválida.")