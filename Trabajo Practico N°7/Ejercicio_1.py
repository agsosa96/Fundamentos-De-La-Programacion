'''
Escribir una funcion para ingresar desde el teclado una serie de numeros entre 1
y 20 guardarlos en una lista. En caso de ingresar un valor fuera de rango el
programa mostrara un mensaje de error solicitara un nuevo numero. Para finalizar
la carga se debera ingresar -1. La funcion no recibe ningun parametro, y
devuelve la lista cargada (o vacia, si el usuario no ingreso nada) como valor de
retorno.
'''

def cargar_lista(lista,num):
    while(num != -1):
        if(num < 1 or num > 20):
            print("Ingrese un valor valido entre 1 y 20")
        else:
            lista.append(num)
        
        num = int(input("Ingrese un numero entre 1 y 20 (Termina con -1): "))
    
    return lista

lista = []

num = int(input("Ingrese un numero entre 1 y 20 (Termina con -1): "))

print(cargar_lista(lista,num))

input()
