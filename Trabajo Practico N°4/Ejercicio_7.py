'''
Leer 10 numeros enteros e imprimir su promedio, el mayor valor leido y en que
posicion se encontraba. Si se ingreso mas de una vez debe informar la primera.
'''

cont = 0

num = int(input("Ingrese un numero: "))
mayor = num
posicion = 1

for i in range(9):
    num = int(input("Ingrese un numero: "))
    cont = cont + 1
    if(num > mayor):
        mayor = num
        posicion = cont
    
print("El mayor numero es: ", mayor)
print("La posicion es: ", posicion)

input()
