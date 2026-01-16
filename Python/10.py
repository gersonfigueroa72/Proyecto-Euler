'''
La suma de los primos menores a 10 es 2 + 3 + 5 + 7 = 17
Encuentre la suma de todos los números primos menores a dos millones
'''
import math

n:int = 2 * 10 ** 6

#Iniciaremos hallando los primos menores a n

primos = [2]

for i in range(3, n, 2):
    div_i = []
    for j in range(2, math.ceil(i**0.5)+1):
        if i % j == 0:
            div_i.append(j)
    if len(div_i) == 0:
        primos.append(i)

print(primos)
print(sum(primos))

