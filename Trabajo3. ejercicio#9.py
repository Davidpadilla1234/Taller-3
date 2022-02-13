"""
datos de entrada
valor de la venta-->valor-->venta
nombre--> n--> cadena
datos de salida
nombre--> n--> cadena
monto compra --> mc --> float
monto a pagar --> mapa --> float
descuento --> des --> float
"""
#entradas
valor = float ( input ( " valor de la venta: " ))
n = cadena ( entrada ( "su nombre:" ))
#cajanegra
compra = ""
si ( valor < 50000 ):
    compra = valor
    des = valor
elif ( valor > 50000  y  valor <= 100000 ):
    compra = valor * 0.95
    des = valor * 0.05
elif ( valor > 100000  y  valor <= 700000 ):
    compra = valor * 0.89
    des = valor * 0.11
elif ( valor > 700000  y  valor <= 1500000 ):
    compra = valor * 0.82
    des = valor * 0.18
elif ( valor > 1500000 ):
    compra = valor * 0.75
    des = valor * 0.25
#salida
print ( "su nombre es" , n )
print ( "su compra fue de:" , valor )
print ( "su compra tendra un valor de: " , compra )
print ( "el decuento fue de: " , des )