'''
Leer un numero entero y mostrar un mensaje informando cuantos digios contiene.
Tener en cuenta que el numero puede ser negativo. Ejemplo: Si se ingresa 12345
se debe imprimir 5.
'''

cont = 0

num = int(input("Ingrese un numero entero (Termina con 0): "))

if(num < 0):
    num = num * (-1)

while(num != 0):
    if(num > 0):
        num = num // 10
        cont = cont + 1

print("La cantidad de digitos del numero es: ",cont)
    
input()
