'''
Realizar un progrograma para ingresar desde el teclado un conjunto de numero. Al
finalizar mostrar por pantalla el primer y ultimo elemento ingresado. Finalizar
la lectura con el valor -1.
'''

num = int(input("Ingrese un numero: "))

if(num != -1):
    primer = num

while(num != -1):
    ultimo = num
    num = int(input("Ingrese un numero: "))

if(num == -1):
    print("No ingreso ningun numero")
else:
    print("El primer numero ingresado es: ",primer)
    print("El ultimo numero ingresado es: ",ultimo)

input()

