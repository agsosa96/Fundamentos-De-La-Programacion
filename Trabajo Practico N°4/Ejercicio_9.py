'''
Se desea analizar cuantos autos circulan con patente con numeracion par y
cuantos con numeracion impar en un dia. escribir un programa que permita
ingresar la terminacion de la patente (entre 0 y 9) hasta ingresar -1 e informe
cuantos vehiculos pasaron con numeracion par y cuantos con numeracion impar.
'''

par = 0
impar = 0
patente = int(input("Ingrese la terminacion de la patente (Termina con -1): "))

while(patente != -1):
    if(patente % 2):
        par = par + 1
    else:
        impar = impar + 1
    patente = int(input("Ingrese la terminacion de la patente (Termina con -1): "))

print("La cantidad de pantentes ingresadas par es: ", par)
print("La cantidad de pantentes ingresadas impar es: ", impar)

input()
    
