'''
Una remiseria requiere un programa que calcule el precio de un viaje a partir de
la cantidad de kilometros que desea recorrer el usuario. Para eso cuenta con la
siguiente tarifa:
    * Viaje minimo de $150
    * Si recorre entre 0 y 10km: $20 por km
    * Si recorre 10km o mas: $15 por km
'''

kilometro = int(input("Ingrese los kilometros quel viaje: "))

if(kilometro < 10):
    tarifa = 150 + kilometro * 20
else:
    tarifa = 150 + kilometro * 15

print("La tarifa que se desea cobrar es de: ",tarifa)
    
input()
