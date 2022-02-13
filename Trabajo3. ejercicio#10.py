"""
datos de entrada
carga --> carga --> str
sueldo --> s --> float
datos de salida
saldo burto --> sd --> float
carga --> carga --> str
"""
#entradas
s = float ( input ( "ingrese su salario: " ))
carga = str ( entrada ( "cual es su carga" ))
#cajanegra
SD = ""
si ( s == 900000 ):
    de = 900000 * 1,60
si ( s == 2000000 ):
    dt = 2000000 * 1,40
si ( s == 3600000 ):
    sd = 3600000 * 1.20
si ( s == 4300000 ):
    dt = 4300000 * 1,15    
si ( s == 5000000 ):
    sd = 5000000 * 1.10    
#salida
print ( "su cargo es" , sd )
print ( "su nuevo salario es: " , sd )