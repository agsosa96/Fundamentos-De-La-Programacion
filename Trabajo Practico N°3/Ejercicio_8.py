'''
Leer tres numero correspondientes al dia, mes y año de una fecha e imprimir un
mensaje indicando si la fecha es valida o no.
'''

dia = int(input("Ingrese el numero de un dia: "))
mes = int(input("Ingrese el numero de un mes: "))
anio = int(input("Ingrese el numero de un anio: "))

if(dia > 0 and dia < 30):
    if(mes > 0 and mes < 13):
        if(mes > 0 and mes < 9999):
            print("La fecha es valida")
        else:
            print("La fecha no es valida")
    else:
        print("La fecha no es valida")
else:
    print("La fecha no es valida")

input()
    
