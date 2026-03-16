
# Exercício 6: Mostre os 10 primeiros números primos.

print("Os 10 primeiros números primos são:", end=" ")

num = 2
j = 0
while j < 10:
    for i in range(2, num):
            if num % i == 0:            
                break
    else:
        print(num, end = " ")
        j += 1
    num += 1
