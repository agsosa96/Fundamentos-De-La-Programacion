'''
Mostrar la tabla de multiplicar (entre 1 y 12) del numero 4.
'''

cont = 1

while(cont < 13):
    print(f'La multiplicacion {cont} * 4 es : {cont * 4}')
    cont = cont +1

'''
Como cambiaria el algoritmo para que el usuario pueda decidir la tabla de
multiplicar a mostrar? 
'''

cont = 1
num = int(input("Ingrese la tabla que desea saber: "))

while(cont < 13):
    print(f'La multiplicacion {cont} * {num} es : {cont * num}')
    cont = cont +1

input()
