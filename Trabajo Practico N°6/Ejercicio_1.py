'''
Escribir una funcion que reciba como parametros dos numeros enteros. Calcular y
devolver el resultado de la multiplicacio nde ambos valores utiluzando solamente
sumas. Por ejemplo 4*3= 4 + 4 + 4.
'''

def multi(num_1,num_2):
    suma = 0
    cont = 0
    while(cont < num_2):
        suma = suma + num_1
        cont = cont + 1

    return suma

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))

multiplicacion = multi(num_1,num_2)

print("La multiplicacion es: ",multiplicacion)

input()
