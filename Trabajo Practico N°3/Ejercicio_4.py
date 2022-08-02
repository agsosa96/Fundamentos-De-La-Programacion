'''
Ingresa las notas de los dos parciales de un alumno e indicar si promociono,
aprobo o si debe recuperar. Informar un error si el valor de alguna nota no esta
entre 0 y 10.
    *Se promociona cuando las notas de ambos parciales son mayores o iguales a 7
    *Se aprueba cuando las notas de ambor parciales son mayores o iguales a 4
    *Se debe recuperar cuando al menos una de las dos notas es menor a 4.
'''

nota_1 = int(input("Ingrese el valor de la primera nota: "))
nota_2 = int(input("Ingrese el valor de la segunda nota: "))

while(nota_1 != -1 and nota_2 != -1):
    if(nota_1 < 0 or nota_1 > 10 or nota_2 < 0 or nota_2 > 10):
        print("Ingrese los valores entre 0 a 10") 
    else:
        if(nota_1 >= 7 and nota_1 <= 10):
            if(nota_2 >= 7 and nota_2 <= 10):
                print("El alumno promociona")
            if(nota_2 >= 4 and nota_2 <= 6):
                print("El alumno aprueba")
            if(nota_2 >= 0 and nota_2 <= 3):
                print("El alumno debe recuperar")
        if(nota_1 >= 4 and nota_1 <= 6):
            if(nota_2 >= 4 and nota_2 <= 10):
                print("El alumno aprueba")
            if(nota_2 >= 0 and nota_2 <= 3):
                print("El alumno debe recuperar")
        if(nota_1 >= 0 and nota_1 <= 3):
            if(nota_2 >= 0 and nota_2 <= 10):
                print("El alumno debe recuperar")         
        
    nota_1 = int(input("Ingrese el valor de la primera nota: "))
    nota_2 = int(input("Ingrese el valor de la segunda nota: "))

input()
