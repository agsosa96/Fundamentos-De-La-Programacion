'''
Crear un programa que pida un numero de mes (por ejemplo 4) y escriba el nombre
del mes en letras ("abril"). Verificar que el mes sea valido y mostrar un
mensaje de error en caso que no lo sea. 
'''

mes = int(input("Ingrese el numero del mes que desea ver (Termina con 0): "))

while(mes != 0):
    if(mes>0 and mes<13):
        if(mes == 1):
            print("El mes es enero")
        if(mes == 2):
            print("El mes es febrero")
        if(mes == 3):
            print("El mes es marzo")
        if(mes == 4):
            print("El mes es abril")
        if(mes == 5):
            print("El mes es mayo")
        if(mes == 6):
            print("El mes es junio")
        if(mes == 7):
            print("El mes es julio")
        if(mes == 8):
            print("El mes es agosto")
        if(mes == 9):
            print("El mes es septiembre")
        if(mes == 10):
            print("El mes es octubre")
        if(mes == 11):
            print("El mes es noviembre")
        if(mes == 12):
            print("El mes es diciembre")
    else:
        print("Ingrese un valor valido entre 1 y 12")
    mes = int(input("Ingrese el numero del mes que desea ver (Termina con 0): "))

input()
