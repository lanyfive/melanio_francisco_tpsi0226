
# Exercício 1: Tipo de dia

dia = input("Informe o Dia: ")
dia = dia.lower()

match dia:
    case "segunda-feira" | "terça-feira" | "quarta-feira" | "quinta-feira" | "sexta-feira":
        print("Dia útil")
    case "sábado" | "sabado" | "domingo":
        print("Fim de semana")
    case _:
        print("Dia inválido")
