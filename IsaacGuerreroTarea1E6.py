#Ejercicio 6
"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
un descuento del 60%. Escribir un programa que comience leyendo el número de
barras vendidas que no son del día. Después el programa debe mostrar el precio
habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste
final total.
"""
PrecioPan = 3.49
#Calcula el monto a pagar con el 60% de descueto
PanConDescuento = PrecioPan * 0.4
#Calcula el Ahorro del pan
DecuentoPanViejo = PrecioPan * 0.6
#El usuario Digital la cantidad a comprar
PanNoDia= int(input ("Ingresar cantidad de barras de pan NO del dia: "))

PrecioTotal = round(PanNoDia * PanConDescuento,2)
DescuentoTotal = round(PanNoDia * DecuentoPanViejo,2)

mensaje = f"""
El precio del pan Fresco es 3.49€, al no ser fresco le danos un descuento del 60%
Precio Total con descuento {PrecioTotal}
Total Ahorrado: {DescuentoTotal}
"""
print(mensaje)