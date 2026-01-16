'''
Un triplete Pitagorico es un conjunto de tres números naturales
a < b < c, para los cuales a**2 + b**2 = c**2
Existe exactamente un triplete Pitagorico implicito para el cual
a + b + c = 1000, encuentre el producto a*b*c
'''

#Iniciaremos hallando los tripletes (a,b,c) tales que su suma de
#1000 y a<b<c.

tripletes = []

for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if a + b +c == 1000 and a < b < c:
                lista = [a,b,c]
                tripletes.append(lista)

print(tripletes)

#Finalmente con estas listas vamos a comprobar si estos tripletes
#cumplen la propiedad pitagorica

for i in tripletes:
    if i[0]**2 + i[1]**2 == i[2]**2:
        producto = i[0]*i[1]*i[2]
        print(producto)
        break

