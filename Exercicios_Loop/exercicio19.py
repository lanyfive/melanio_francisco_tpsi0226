# Exercícios 19: Mostre os primeiros 60 números da Sequência de Fibonacci.

a = 0
b = 1
num = 0
print(f"Sequência de Fibonacci: {a} {b}", end=" ")
for i in range(2, 60):
    num = a + b
    a = b
    b = num
    print(num, end=" ")


