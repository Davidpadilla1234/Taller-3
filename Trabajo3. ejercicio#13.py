"""
entradas
dia--> int -->d
mes--> int -->m
año--> int -->a
salidas
sinno-->str->sig
edad--> int -->edad
"""
#entradas
d  = int ( input ( 'Digite el numero de dia:' ))
m  = int ( input ( "Digite el numero de mes:" ))
a = int ( entrada ( "año de nacimiento:" ))
#cajanegra
edad = 2022 - un
sig = ""
si ( d >= 21  y  m == 1 ) o ( d <= 19  y  m == 2 ):
    sig = ( 'Acuario' )
elif ( d >= 20  y  m == 2 ) o ( d <= 20  y  m == 3 ):
    sig = ( 'Piscis' )
elif ( d >= 21  y  m == 3 ) o ( d <= 20  y  m == 4 ):
    sig = ( 'Aries' )
elif ( d >= 21  y  m == 4 ) o ( d <= 21  y  m == 5 ):
    sig = ( 'Tauro' )
elif ( d >= 22  y  m == 5 ) o ( d <= 21  y  m == 6 ):
    sig = ( 'Géminis' )
elif ( d >= 21  y  m == 6 ) o ( d <= 23  y  m == 7 ):
    sig = ( 'Cáncer' )
elif ( d >= 24  y  m == 7 ) o ( d <= 23  y  m == 8 ):
    sig = ( 'Leo' )
elif ( d >= 24  y  m == 8 ) o ( d <= 23  y  m == 9 ):
    sig = ( 'Virgo' )
elif ( d >= 24  y  m == 9 ) o ( d <= 23  y  m == 10 ):
    sig = ( 'Libra' )  
elif ( d >= 24  y  m == 10 ) o ( d <= 22  y  m == 11 ):
    sig = ( 'Escorpio' )
elif ( d >= 23  y  m == 11 ) o ( d <= 21  y  m == 12 ):
    sig = ( 'Sagitario' )
elif ( d >= 22  y  m == 12 ) o ( d <= 20  y  m == 1 ):
    sig = ( 'Capricornio' )
#salida
print ( "su signo es: " , str ( sig ))
print ( "su edad es" , int ( edad ))