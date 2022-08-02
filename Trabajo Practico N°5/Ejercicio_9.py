'''
Ingresar un numero N y validar que sea positivo. Luego:
    a) Mostrar los primeros numeros impares, hasta alcanzar el numero ingresado.
    b) Informar la suma de esos numeros impares.

Ejemplo:
    * Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
    * Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
    * Si se ingresa -5, se pedir otro numero.
'''

suma = 0

num = int(input("Ingrese un numero positivo: "))

while(num < 0):
    print("Ingrese un numero positivo")
    num = int(input("Ingrese un numero positivo: "))

for i in range(num + 1):
    impar = i % 2
    if(impar != 0):
        print(i)
        suma = suma + i

print("La suma de los numeros impares es: ", suma)

input()
