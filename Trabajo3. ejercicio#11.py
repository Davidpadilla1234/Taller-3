"""
datos de entrada
temperatura---> t ---> flotar
datos de salida
deporte --> deporte
"""
#entradas
t = flotador ( entrada ( "temperatura en f°: " ))
#cajanegra
deportes = ""
si ( t > 85  y  t <= 120 ):
    deporte = "natacion"
elif ( t > 70  y  t <= 85 ):
    deporte = "tenis"
elif ( t > 32  y  t <= 70 ):
    deporte = "golf"
elif ( t > 10  y  t <= 32 ):
    deporte = "esqui"
elif ( t > 0  y  t <= 10 ):
    deporte = "marcha"
más :
    deporte = "no se encuentra en el rango"  
#salida
print ( "su deporte es:" , deporte )