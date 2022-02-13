"""
datos de entrada
sueldo del trabajador --> sd --> float
datos de salida
nuevo sueldo -->ns--> float
"""
#entradas
sd = float ( input ( "ingrese su sueldo:" ))
#cajanegra
si ( sd <= 900000 ):
    ns = sd * 1.15
elif ( sd > 900000 ):
    ns = sd * 1.12
#salida
print ( "su nuevo sueldo es:" , ns )