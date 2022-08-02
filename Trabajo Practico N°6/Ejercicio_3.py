'''
Imprimir una columna de asteriscos, Donde su altura se recibe como parametro.
'''

def columna(num_1):
    num_1 = print("*")
    return num_1

num_1 = int(input("Ingrese un numero para la altura de la columna: "))

for i in range(num_1):
    print(columna(num_1))
