"""
datos de entrada
cuanto vieron los tres departamentos -->v -->float
salario basico de los vendedores -->s -->float
ventas del departamento 1 -->v1 -->float
ventas del departamento 2 -->v2 -->float
ventas del departamento 3 -->v3 -->float
datos de salida
salario del vendedor 1 --> p1
salario del vendedor 2 --> p2
salario del vendedor 3 --> p3
"""
#entradas
v = float ( input ( "¿cuanto vio los tres departamentos? " ))
s = float ( input ( "salario basico de los vendedores" ))
v1 = float ( entrada ( "ventas del departamento 1" ))
v2 = float ( entrada ( "ventas del departamento 2" ))
v3 = float ( entrada ( "ventas del departamento 3" ))
p1 = (( v1 * 100 ) / v )
p2 = (( v2 * 100 ) / v )
p3 = (( v3 * 100 ) / v )
s2 = s * 1.02
#cajanegra
si ( p1 > 33 ):
    print ( "salario del vendedor 1" , s2 )
más :
    print ( "salario del vendedor 1" , s )
si ( p2 > 33 ):
    print ( "salario del vendedor 2" , s2 )
más :
    print ( "salario del vendedor 2" , s )
si ( p3 > 33 ):
    print ( "salario del vendedor 3" , s2 )
más :
    print ( "salario del vendedor 3" , s )
