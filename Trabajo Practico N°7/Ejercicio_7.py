'''
Idem anterior, utilizando busqueda binaria sobre una lista ordenada.
'''

def cargar_lista(lista,num):
    while(num != -1):
        lista.append(num)
        num = int(input("Ingrese un numero (Termina con -1): "))

    return lista

def bubble_sort(lista):
    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[j] < lista[i]):
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
                
    return lista

def busqueda_binaria(lista, valor):
  posicion = -1
  izq = 0
  der = len(lista)-1
  while (izq <= der and posicion == -1):
    mitad = (izq + der) // 2
    if (lista[mitad] == valor):
      posicion = mitad
    else:
      if (valor > lista[mitad]):
        izq = mitad + 1
      else:
        der = mitad - 1
        
  return posicion


array = []

num = int(input("Ingrese un numero (Termina con -1): "))

cargar_lista(array,num)
bubble_sort(array)

valor = int(input("Ingrese el valor que desea buscar: "))

posicion = busqueda_binaria(array,valor)

print(array)
print(posicion)

input()


