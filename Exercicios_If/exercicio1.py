
# Exercício 1: Converter Segundos em Horas, Minutos e Segundos

segundos = int(input("Digite o total de segundos: "))
print(f"{segundos} segundos equivalem a", end="")

horas = segundos // 3600
resto_segundos = segundos % 3600
minutos = resto_segundos // 60
segundos = resto_segundos % 60
print(f" {horas} horas, {minutos} minutos e {segundos} segundos.")
