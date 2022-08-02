'''
Una empresa aplica el siguiente procedimiento en la comercializacion de sus
productos:
    * Aplica el precio vase a la primera docena de unidades.
    * Aplica un 10% de descuento a todas las unidades entre 13 y 100.
    * Aplica un 25% de descuento a todas las unidades por encima de las 100.

Por ejemplo, supongamos que vende 230 unidades de un prodecto cuyo precio base
es 100. El calculo resultante seria:

                    100 * 12 + 90 * 88 + 75 * 130 = 18870
                y el precio promedio es de 18870 / 230 = 82.04
                
Escribir un programa que lea la cantidad solicitada de un producto y su precio
base, y muestre el valor total de la venta y el precio promedio por unidad. El
fin de carga se determana ingresando -1 como cantidad solicitada. Al finalizar
informar:
    * Cantidad de ventas realizadas total.
    * Cantidad de ventas en las que se aplico un 10% de desceunto.
    * Cantidad de ventas en las que SOLO se aplico el precio base, es decir
      que no se le realizaron descuentos.
'''
