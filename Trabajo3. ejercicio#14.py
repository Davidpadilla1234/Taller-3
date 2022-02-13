"""
datos de entrada
lectura_actual-->lac-->
lectura_anterior-->lan-->
datos de salida
costo-->c-->int
"""
#entradas
desde el  constructor de importación copyreg  
lac = int ( entrada ( "lectura actual:" ))
lan = int ( entrada ( "lectura anterior:" ))
#cajanegra
d = lan - lac
costo = ""
si ( d > 0  y  d <= 100 ):
    costo = d * 4600
si ( d >= 101  y  d <= 300 ):
    costo = d * 80000
si ( d >= 301  y  d <= 500 ):
    costo = d * 100000
si ( d >= 501 ):
    costo = d * 120000
#salida
print ( "su costo sera: " , costo )