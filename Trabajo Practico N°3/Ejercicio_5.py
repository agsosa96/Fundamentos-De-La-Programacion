'''
Una editorial determina el precio de un libro segun la cantidad de paginas que
contiene. El costo basico es de $500, mas $3,20 por pagina con encuadernacion
rustica. Si el numero de paginas supera las 300, la encuadernacion debe ser en
tela, lo que incrementa el costo en $200. Ademas si el numero de paginas
sobrepasa las 600 se hace necesario un precedimiento especial de encuadernacion
que incrementa el costo en otros $336. Desarrolar un programa que calcule el
costo de un libro dado el numero de paginas. 
'''

paginas_libro = int(input("Ingrese las paginas de su libro para encuerdenar: "))

if(paginas_libro < 300):
    costo = 500 + 3.2 * paginas_libro
elif(paginas_libro < 600):
    costo = 500 + 3.2 * paginas_libro + 200
else:
    costo = 500 + 3.2 * paginas_libro + 200 + 336

print("El costo del encuardernado es: ",costo)

input()
