'''
El factorial de un numero entero N mayor que cero de define como el producto de
todos los enteros X tales que 0 < x <= N. Desarrolar un programa para calcular
el factorial de un numero dado. Deberan rechazarse las entradas invalidas
(menores que 0)
'''

factorial = 1

num = int(input("Ingrese el numero del cual quiere saber el factorial: "))

while(num < 0):
    print("Ingrese un numero mayor o igual a 0")
    num = int(input("Ingrese el numero del cual quiere saber el factorial: "))


while(num > 0):
    factorial = factorial * num
    num = num - 1

print("El fatorial del numero es: ",factorial)

input()
