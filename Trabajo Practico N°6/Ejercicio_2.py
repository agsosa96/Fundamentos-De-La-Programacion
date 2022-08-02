'''
Dados dos parametros enteros A y B, obtener A^B (A elevado a la B) mediante
multiplicaciones sucesivas, utilizando la funcion del ejercicio anterior para
multiplicar. Por ejemplo 4^3 = 4 * 4 * 4.
'''

def pote(num_1,num_2):
    multi = 1
    cont = 0
    while(cont < num_2):
        multi = multi * num_1
        cont = cont + 1

    return multi

num_1 = int(input("Ingrese el numero que quiere que sea la base: "))
num_2 = int(input("Ingrese el numero que quiere que sea la potencia: "))

potencia= pote(num_1,num_2)

print("El resultado es: ",potencia)

input()
