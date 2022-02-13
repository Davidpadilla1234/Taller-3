"""
datos de entrada
inversión
reinversión de intereses
datos de salida
dinero total
valor de las ganancias
valor total
"""
#entradas
inversión = float ( input ( "mayúsculas invertidas:" ))
i = float ( entrada ( "tasa de intereses:" ))
#cajanegra
p = inversión * ( i / 100 )
total = (( p + inversión ) * i )
intereses = ""
si ( 100000 < p ):  
    print ( "el valor de las ganancias es" , str ( p ))
más :
    print ( "el valor de la cuenta es" , str ( total ))