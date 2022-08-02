'''
Devolver True si el numero entero recibe como primer parametro es multiplo del
segundo, o False en caso contrario. Ejemplo: esmultiplo(40,8) devuelve True y
esmultiplo(50,3) devuelve False.
'''

def multiplo(num_1,num_2):
    if((num_1 % num_2) == 0):
        multi = True
    else:
        multi = False
        
    return multi

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese el segundo numero para saber si es multiplo: "))

print("El resultado es:",multiplo(num_1,num_2))

input()
