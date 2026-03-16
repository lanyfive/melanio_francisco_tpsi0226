
# Exercício 12: Tabuada (Soma, Subtracção, Divisão, Multiplicação) do número N até N-1 Vezes.

num = int(input("Introduza um número: "))
print(f"   SOMA         SUBTRACÇÃO       DIVISÃO     MULTIPLICAÇÃO")
num_operations = 0
for i in range (1, num):
    print(f"{num} + {i} = {num + i}", end="      ")
    print(f"{num} - {i} = {num - i}", end="      ")
    print(f"{num} / {i} = {(num / i):.2f}", end="      ")
    print(f"{num} * {i} = {num * i}")
    num_operations += 4

print(f"\nForam efetuadas um total de {num_operations} operações de cálculo.")