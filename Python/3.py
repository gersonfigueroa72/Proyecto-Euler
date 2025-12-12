'''
Los factores primos de 13195 son 5, 7, 13 y 29.
Cuál es factor primo más grande del número 600851475143 
'''

#n será el número del cual hallaremos todos sus factores primos
#Debemos factorizar n es sus factores primos

import math

n = 600851475143
factores_primos_n = []
temp = n

if n % 2 == 0:
    for i in range(2, math.ceil(n**0.5) + 1):
        while temp % i == 0:
            factores_primos_n.append(i)
            temp /= i

    # Si al final temp queda mayor que 1 entonces, no tuvo ningun
    # divisor, por lo que temp = n es un primo y sería el único factor
    # a agregar en factores_primos_n
    if temp > 1:
        factores_primos_n.append(temp)

    print(factores_primos_n)    
else:
    for i in range(3, math.ceil(n**0.5) + 1, 2):
        while temp % i == 0:
            factores_primos_n.append(i)
            temp /= i

    # Si al final temp queda mayor que 1 entonces, no tuvo ningun
    # divisor, por lo que temp = n es un primo y sería el único factor
    # a agregar en factores_primos_n
    if temp > 1:
        factores_primos_n.append(temp)

    print(factores_primos_n)
