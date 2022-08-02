'''
Ingresar numeros, hasta que la suma de las numeros pares supere 100. Mostrar
cuantos numeros se ingresaron en total.
'''

cont = 0
suma = 0

num = int(input("Ingrese un numero (Termina cuando la suma supera los 100) : "))

while(suma < 100):
    suma = suma + num
    cont = cont + 1
    if(suma < 100):
        num = int(input("Ingrese un numero (Termina cuando la suma supera los 100) : "))

print("La cantidad de numeros ingresados son: ", cont) 

input()
