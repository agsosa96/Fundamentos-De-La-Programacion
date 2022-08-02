'''
Realizar un programa para ingresar desde el teclado un conjunto de numeros e
informar si la cantidad de elementos es impar o par, sin utilizar contadores.
Finalizar la lectura de datos con el calor -1.
'''

num = int(input("Ingrese un numero (Termina con -1): "))

cantidad = True

while(num != -1):
    if(cantidad == True):
        cantidad = False
    else:
        cantidad = True
    num = int(input("Ingrese un numero (Termina con -1): "))


if(cantidad == True):
    print("La cantidad fue par")
else:
    print("La cantidad fue impar")

input()
