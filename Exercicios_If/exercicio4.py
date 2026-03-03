
# Exercício 4: Verificar se o Cheque Pode Ser Descontado

saldo = float(input("Digite o saldo da conta: "))
cheque = float(input("Digite o valor do cheque: "))

if cheque > saldo:
    print("O cheque não pode ser descontado.")
else:
    saldo -= cheque
    print(f"Cheque descontado. Saldo: {saldo:.2f}")
