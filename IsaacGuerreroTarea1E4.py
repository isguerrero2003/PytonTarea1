#Ejercicio 4
"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada
paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
programa que lea el número de payasos y muñecas vendidos en el último pedido y
calcule el peso total del paquete que será enviado.
"""
PayasosPeso = 112
MunecasPeso = 75

VentaPayasos = int(input ("Ingresar la cantidad de Payasos a Comprar : "))
VentaNunecas = int(input ("Ingresar los años de Muñecas a Comprar : "))

EnvioPayaso = PayasosPeso * VentaPayasos
EnvioMunecas = MunecasPeso * VentaNunecas
TotalEnvio = EnvioPayaso + EnvioMunecas

print("El peso total del pedido es : ", TotalEnvio)