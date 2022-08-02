'''
Leer numeros que representan edades de un grupo de personas, finalizando la
lectura cuando se ingrese el numero -1. Imprimir cuantos son menores de 18 años,
cuantos tienen 18 a;os o mas y el promedio de edad de ambos grupos. Descartar
valores que no representan una edad valida. (Se considera valida una edad entre
0 y 100)
'''

contador_menor_edad = 0
contador_mayor_edad = 0
suma_menor_edad = 0
suma_mayor_edad = 0


edad = int(input("Ingrese una edad (Termina con -1): "))

while(edad != -1):
    if(edad < 0 or edad > 100):
        print("Ingrese una edad validad entre 0 y 100")
    else:
        if(edad < 18):
            contador_menor_edad = contador_menor_edad + 1
            suma_menor_edad = suma_menor_edad + edad
        else:
            contador_mayor_edad = contador_mayor_edad + 1
            suma_mayor_edad = suma_mayor_edad + edad
    edad = int(input("Ingrese una edad (Termina con -1): "))

print("La cantidad de menores de edad ingresados son: ",contador_menor_edad)
print("La cantidad de menores de edad ingresados son: ",contador_mayor_edad)
print("La cantidad de menores de edad ingresados son: ",suma_menor_edad / contador_menor_edad)
print("La cantidad de menores de edad ingresados son: ",suma_mayor_edad / contador_mayor_edad)

input()

