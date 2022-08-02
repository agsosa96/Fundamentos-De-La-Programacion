'''
Rellenar una lista con numeros enteros entre 0 y 100 obtenidos al azar e
imprimir el valor minimo y el lugar que ocupa. Tener en cuenta que el minimo
puede estar repetido, en cuyo caso deberan mostrarse todas las posiciones que
ocupe. La carga de datos termina cuando se obtenga un 0 como numero al azar, el
que no debera cargarse en la lista.
'''

def cargar_lista(lista,num):
    while(num != -1):
        if(num < 0 or num > 100):
            print("Ingrese un numero entre 0 y 100")
        else:
            lista.append(num)
        num = int(input("Ingrese un numero (Termina con -1): "))

    return lista

lista = []

num = int(input("Ingrese un numero (Termina con -1): "))

valor = cargar_lista(lista,num)

print(lista)
