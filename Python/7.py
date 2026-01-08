'''
Enumerando los primeros seis números primos:
2,3,5,7,11,13
Podemos ver que el sexto primo es 13 
Cúal es el primo número 10,001
'''
import math

primos = [2]
i = 3
while len(primos) < 10001:
    divisores_i = []
    for j in range(1,math.ceil((i+1)**0.5)):
        if i % j == 0:
            divisores_i.append(j)
    if len(divisores_i) == 1:
        primos.append(i)
    i = i + 2

print(primos[-1])
