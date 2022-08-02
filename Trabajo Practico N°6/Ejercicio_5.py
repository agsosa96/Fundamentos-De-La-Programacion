'''
Desarollar la funcion signo(n), que reciba un numero entero y devuelva 1, -1 o 0
segun el valor recibido sea positivo, negatico o nulo.
'''

def signo(num):
    if(num > 0):
        valor = 1
    if(num < 0):
        valor = -1
    if(num == 0):
        valor = 0

    return valor

num = int(input("Ingrese un numero para saber su signo: "))

print("El signo es: ",signo(num))

input()
