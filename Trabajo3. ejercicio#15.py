"""
datos de entrada
hemoglobina-->hmn-->int
edad-->edad-->int
sexo-->sx-->srt
datos de salida
"""
#entradas
edad = int ( input ( "indique su edad en meses:" ))
sx = int ( input ( " indica tu sexo en femenino como 1 o masculino como 2 : " ))
hmn = int ( entrada ( "nivel de hemoglobina:" ))
#cajanegra
si ( edad > 0  y  edad <= 1 ) y ( hmn >= 13  y  hmn <= 26 ):
    anm = "no tiene anemia"
elif ( edad > 1  y  edad <= 6 ) y ( hmn >= 10  y  hmn <= 18 ):
    anm = "no tiene anemia"
elif ( edad > 6  y  edad <= 12 ) y ( hmn >= 11  y  hmn <= 15 ):
    anm = "no tiene anemia"
elif ( edad > 12  y  edad <= 60 ) y ( hmn >= 11.5  y  hmn <= 15 ):
    anm = "no tiene anemia"
elif ( edad > 60  y  edad <= 120 ) y ( hmn >= 12.6  y  hmn <= 15.5 ):
    anm = "no tiene anemia"
elif ( edad > 180 ) y ( hmn >= 12  y  hmn <= 16 ) y ( sx == 1 ) :
    anm = "no tiene anemia"
elif ( edad > 180 ) y ( hmn >= 14  y  hmn <= 18 ) y ( sx == 2 ) :
    anm = "no tiene anemia"
más :
    anm = ( "tiene anemia" )    
#salida
imprimir ( "" , anm )