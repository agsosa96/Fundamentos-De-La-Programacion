'''
Escribir una funcion para devolver una lista con todas las posiciones que ocupa
un valor pasado como parametro, utilizando busqueda secuencial en una lista
desordenada. La funcion debe devolver una lista vacia si el elemento no se
encuentra en la lista original.
'''

def cargar_lista(lista,num):
    while(num != -1):
        lista.append(num)
        num = int(input("Ingrese un numero (Termina con -1): "))

    return lista

def busqueda_secuencial(lista,valor):
    i = 0
    while(i < len(lista)):
        if(lista[i] == valor):
            posicion.append(i)
        i = i + 1

    return posicion

lista = []
posicion = []

num = int(input("Ingrese un numero (Termina con -1): "))

cargar_lista(lista,num)

valor = int(input("Ingrese el valor que desea buscar: "))

busqueda_secuencial(lista,valor)

print(lista)
print(posicion)

input()
