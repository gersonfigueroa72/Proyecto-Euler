''''
2520 es el número más pequeño que puede dividir a cada uno de los números del 1 al 10 sin ningun residuo.
Cúal es el número positivo más pequeño que divide a todos los números del 1 al 20"
'''

n=2520 #este será el primer número que supondremos divide a todos los números del 1 al 20 (aunque no sea cierto)
n_iteracion = n

while True:
    comprobacion = [] #acá almacenaremos los divisores de n_iteracion
    for i in range(2,21): #no hace falta verificar el 1
        if n_iteracion % i == 0:
            comprobacion.append(i)
    if len(comprobacion) == 19:
        print(n_iteracion)
        break
    else:
        n_iteracion += 20 #vamos de 20 en 20, ya que el número debe ser multiplo de 20













