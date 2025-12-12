#PROBLEMA 2 - PROYECTO EULER
""""
Cada nuevo termino en la secuencia Fibonacci es generado
sumando los dos terminos anteriores. Si empezamos en 
con los números 1 y 2, los primeros 10 términos de la 
secuencia es 1,2,3,5,8,13,21,34,55,89,...
Considerando los términos de la secuencia de Fibonacci cuyos
valores no superan los cuatro millones, encuentre la suma de 
los términos pares.
"""

#Iniciaremos generando la secuencia Fibonacci menor a un número n

n:int = 4000000 #número hasta donde llegará la secuencia
sec_fib = [] #Lista donde se guardará la sec. fibonacci
sec_fib_par = [] #Lista donde se guardará la sec. fibonacci par

fib1 = 1
fib = 0

while fib <= n:
    sec_fib.append(fib)
    fib1, fib = fib, fib + fib1 #Se evaluan simultaneamente las condiciones, i.e
    #fib1, fib = 0, 0 + 1
    #fib1, fib = 1, 1 + 0 #usa los valores anteriores
    #fib1, fib = 2, 2 + 1 
    #fib1, fib = 3, 3 + 2
    #fib1, fib = 5, 5 + 3
print(sec_fib)

#Ahora seleccionaremos solamente los números pares en la sec. Fibonacci:

for i in sec_fib:
    if i % 2 == 0:
        sec_fib_par.append(i)

print(sec_fib_par)

#Ahora sumamos todos los valores de sec_fib_par

print(sum(sec_fib_par))



    


