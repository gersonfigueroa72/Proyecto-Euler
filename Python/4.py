'''
Un número palindrómico se lee igual en ambos sentidos. El número palindrómico más 
grande, hecho por el producto de dos números de dos dígitos es 9009 = 91 * 90.
Encuentre el número palindrómico más grande creado por dos números de 3 dígitos.
'''

#Haremos un programa que encuentre todos los números palindrómicos para números de 3 cifras.
palindromos = []

for i in range(1,1000):
    for j in range(i,1000): #Iniciar desde i permite no repetir multiplicaciones
        digitos = []
        mult = i * j
        
        for k in str(mult):
            digitos.append(k)
        
        digitos_inv = digitos[::-1] #invertimos la lista

        if digitos == digitos_inv:
            num_palindromo = ''.join(digitos) #Concatenamos
            palindromos.append(int(num_palindromo))

print(max(palindromos))
        
