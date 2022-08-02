'''
Escribir una funcion comparar(a,b) que reciba como parametro dos numeros enteros
y devuelva 1 si el primer es mayor que el segundo, 0 si son iguales o -1 si el
primero es menor que el segundo. En este ejercicio debe aprovecharse la funcion
del ejercicio anterior. Ejemplo: comprar(4,2) devuelve 1, y comprar(2,4)
devuelve -1.
'''

def comparar(num_1,num_2):
    if(num_1 > num_2):
        compara = 1
    if(num_1 < num_2):
        compara = -1
    if(num_1 == num_2):
        compara = 0
    return compara

num_1 = int(input("Ingrese el primer numero que desea comparar: "))
num_2 = int(input("Ingrese el segundo numero que desea comparar: "))

print("La comparacion dio como resultado: ",comparar(num_1,num_2))

input()
