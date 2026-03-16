
# Exercício 15: Escreva no ecrã todas as linhas de código ASCII(0 a 255) e o código correspondente. 
# Dispor de 20 em 20 com a condição de continuação ou saída do programa.

i = 0
while i <= 255:
    j = 0
    while j < 20 and i <= 255:
        print(i, "-", chr(i))
        i += 1
        j += 1

    if i <= 255:
        opcao = input("Deseja continuar? (S/N): ")
        if opcao.lower() != "s":
            break
