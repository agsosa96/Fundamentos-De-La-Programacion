'''
Leer un numero entero e imprimir un mensaje indicando si es par o impar.
'''

num_1 = int(input("Ingrese un numero (Solo numeros positivos): "))

par = num_1 % 2

if(par == 0):
    print("El numero es par")
else:
    print("El numero es impar")

input()
