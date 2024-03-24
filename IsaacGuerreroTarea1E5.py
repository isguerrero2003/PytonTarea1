#Ejercicio 5
"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la
cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a
dos decimales.
"""

Ahorro = int(input ("Ingresar el monto del ahorro : "))

PrimerAno = round(Ahorro * 1.04,2)
SegundoAno = round(PrimerAno * 1.04,2)
TercerAno = round(SegundoAno * 1.04,2)
print("Recuerde que manejamos un interes anual del $4 capitalizables a 3 años" )
print("Ahorro Primer año : ", PrimerAno)
print("Ahorro Primer año : ", SegundoAno)
print("Ahorro Primer año : ", TercerAno)