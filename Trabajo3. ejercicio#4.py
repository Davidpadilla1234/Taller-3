"""
datos de entrada
costo de las piezas--> c --> float
datos de salida
inversión --> i -->str
prestamo --> p -->str
crédito --> cre -->str
intereses --> int -->str
"""
#entradas
c = float ( input ( "cosot de las piezas: " ))
#cajanegra
si ( c >= 5000000 ):
    yo = c * 0.55
    p = c * 0,30
    cre = c * 0.15
    int = 0
más :
    yo = c * 0.70
    p = 0
    cre = c * 0.30
    int = cre * 0.20
#salida
print ( "el precio de la inversion es" ,   str ( i ))
print ( "el precio del prestamo" , str ( p ))
print ( "el precio del credito" , str ( cre ))
print ( "el precio del interes" , str ( int ))