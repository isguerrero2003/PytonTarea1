#Ejercicio 3
import math
"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión.
cantidad por (interés dividido 100 más 1) elevado años"""

inversion = int(input ("Ingresar la cantidad a invertir : "))
anhos = int(input ("Ingresar los años de la inversion : "))
interes = int(input ("Ingresar el interes anual : "))
PorcentajeInteres = (interes / 100) + 1


porcentajeelevadoanhos = math.pow(PorcentajeInteres,anhos)
capital = inversion * porcentajeelevadoanhos
print("Capital Obtenido : ", capital)
