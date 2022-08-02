'''
Leer un numero correpondiente a un año e imprimir un mensaje indicando si es
bisiensto o no. Un año es bisiesto cuando es divisible por 4. Sin embargo,
aquellos años que sean divisibles por 4 y tambien por 100 no son bisiestos, a
menos que tambien sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto
pero si el 2000.
'''

año = int(input("Ingrese el año para saber si es bisiesto: "))

if(año % 4 == 0 and año % 400 == 0):
    if(año % 100 == 0):
        print("El año es bisiesto")
else:
    print("El año no es bisiesto")

input()
