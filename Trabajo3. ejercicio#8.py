"""
datos de entrada
P-->p-->int
Q-->q-->int
datos de salida
"""
#entradas
P = int ( entrada ( "ingrese valor de P: " ))
Q = int ( entrada ( "ingrese valor de Q: " ))
#cajanegra
h = ( PAG ** 3 ) + ( Q ** 4 ) - ( 2 * PAG ** 2 )
ecuacion = ""
si ( h > 680 ):
    print ( "satisfacen la expresion" , Q , P )
elif ( h < 680 ):
    print ( "no satisface la expresion" , Q , P )
#salida
print ( "el resultado es ademas" , h )