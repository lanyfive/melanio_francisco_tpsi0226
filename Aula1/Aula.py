
print("Hello, World!")

a = int(input("Digite um número: "))
print("O número digitado foi:", a)
 
tupla = (1, 2, 3, "r", 5)
print(tupla[3])

val1 = 2
val2 = 3
val3 = 5

if  val1 == val2 == val3:
    print("Os três valores são iguais.")
elif val1 >= val2 and val2 >= val3:
    print(f"O maior valor é Val1 = {val1} e o menor valor é Val3 = {val3}")
elif val1 >= val3 and val3 >= val2:
    print(f"O maior valor é Val1 = {val1} e o menor valor é Val2 = {val2}")
elif val2 >= val1 and val1 >= val3:
    print(f"O maior valor é Val2 = {val2} e o menor valor é Val3 = {val3}")
elif val2 >= val3 and val3 >= val1:
    print(f"O maior valor é Val2 = {val2} e o menor valor é Val1 = {val1}")
elif val3 >= val1 and val1 >= val2:
    print(f"O maior valor é Val3 = {val3} e o menor valor é Val2 = {val2}")
elif val3 >= val2 and val2 >= val1:
    print(f"O maior valor é Val3 = {val3} e o menor valor é Val1 = {val1}")
