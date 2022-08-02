'''
Escribir una funcion para devolver la primera posiscion que ocupa un valor
pasado como parametro, utilizando busqueda secuencial en una lista desordenada.
La funcion debe devolver -1 si el elemento no se encuentra en la lista.
'''

def cargar_lista(lista,num):
    while(num != -1):
        lista.append(num)
        num = int(input("Ingrese un numero (Termina con -1): "))
        
    return lista

def busqueda_secuencial(lista,valor):
    posicion = -1
    i = 0
    while(i < len(lista) and posicion == -1):
        if(lista[i] == valor):
            posicion = i
        i = i + 1
        
    return posicion

lista = []

num = int(input("Ingrese un numero (Termina con -1): "))

cargar_lista(lista,num)

valor = int(input("Ingrese el valor que desea buscar: "))

posicion = busqueda_secuencial(lista,valor)

print("La posicion del valor que desea buscar: ", posicion)

input()
