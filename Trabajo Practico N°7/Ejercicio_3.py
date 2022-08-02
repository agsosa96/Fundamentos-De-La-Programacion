'''
Calcular la suma de los numero de la lista.
'''

def cargar_lista(lista,num):
    while(num != -1):
        lista.append(num)
        num = int(input("Ingrese un numero (Termina con -1): "))
    
    return lista

def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]

    return suma

lista = []

num = int(input("Ingrese un numero (Termina con -1): "))

cargar_lista(lista,num)

print("La suma de los numero de la lista es: ",suma_lista(lista))

input()
