#PROBLEMA 1 - PROYECTO EULER
"""
Si nosotros enlistamos todos los numeros naturales menores a 10 que son tambien
multiplos de 3 o 5, nosotros obtenemos a los números 3,5,6,9.
La suma de estos multiplos es 23.
Encuentre la suma de todos los multiplos de 3 o 5 menores que 1000.
"""

#Sea n, un numero natural, tal que hallaremos todos los multiplos de 3 o 5
#menores a él.

n:int = 1000
multiplos = []
#Hallaremos ahora los multiplos 3 o 5 menores a n:

for i in range(1,n):
    if i%3==0:
        multiplos.append(i)
    elif i%5==0:
        multiplos.append(i)

suma = sum(multiplos)
print(f"La suma de los multiplos de 3 y 5 \n menores a {n} es: {suma}")



