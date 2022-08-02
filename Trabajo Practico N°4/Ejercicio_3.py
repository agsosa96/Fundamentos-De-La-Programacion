'''
Realizar un programa para ingresa desde el teclado un conjunto de numeros y
mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos
con un calor -1.
'''

num = int(input("Ingrese un numero (Termina con -1): ")) 

if(num != -1):
    minimo = num
    maximo = num

while(num != -1):
    if(num > maximo):
        maximo = num
    if(num < minimo):
        minimo = num
    num = int(input("Ingrese un numero (Termina con -1): "))

if(num == -1):
    print("No ingreso ningun numero")

print("El minimo numero es: ",minimo)
print("El maximo numero es: ",maximo)

input()
