
# Exercícios 17: Determine os múltiplos de 5 mas não múltiplos de 3
# De 1 a 1000 deve ser a sequência.
list_mult5 = []
for i in range(1, 1001):
    mult5 = 5 * i
    if mult5 % 3 != 0: list_mult5.append(mult5)

print(f"Múltiplos de 5 (mas NÂO de 3): {list_mult5}")