'''
La suma de los cuadrados de los primeros diez números es:
1^{2} + 2^{2} + ... + 10^{2} = 385

El cuadrado de la suma de los primeros diez números naturales es,
(1 + 2 + 3 ... 10)^{2} = 3025
Por lo tanto, la diferencia entre la suma de los cuadrados 
de los primeros diez números naturales y el cuadrado de la suma es
3025-385 = 2640

Encuentra la diferencia entre la suma de los cuadrados de los primeros 
cien números naturales y el cuadrado de la suma.
'''

cuadrados1 = [] #Acá almacenamos la suma de los cuadrados

#Iniciamos hallando la suma de cuadrados1

for i in range(1,101):
    cuadrados1.append(i**2)

suma_cuadrados1 = sum(cuadrados1)


#Hallamos ahora la suma de cuadrados2

lista_al_100 = list(range(1,101)) #creamos una lista del 1 al 100

suma_al_100 = sum(lista_al_100) #Para números más grandes usar la suma de Gauss

suma_cuadrados2 = suma_al_100**2

#Por último restamos

resta_cuadrados = suma_cuadrados2 - suma_cuadrados1
print(resta_cuadrados)


