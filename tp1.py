
#Punto 1:Generá una estructura que almacene los datos de cada columna: nombre, el tipo 
#de dato y el porcentaje de completitud de cada una.

columnas = {
    'PONDERA': ['int', 95.0],
    'ESTADO': ['int', 80.0],
    'CAT_OCUP': ['int', 70.0],
    'EDAD': ['int', 100.0],
    'REGION': ['int', 98.5],
    'AGLOMERADO': ['int', 98.5],
    'MAS_500': ['string', 60.0],
    'ANO4': ['int', 100.0],
    'TRIMESTRE': ['int', 100.0],
    'ITF': ['int', 45.0],
    'GDECCFR': ['int', 50.0]
}

#Punto 2:

roles = {
    'docente': {
        'columnas': ['EDAD', 'ESTADO', 'REGION', 'AGLOMERADO'],
        'criterio': 'nombre',        # Ordenado alfabéticamente
        'orden': 'A',                # Ascendente
        'umbral': None               
    },
    'investigador': {
        'columnas': ['PONDERA', 'ESTADO', 'CAT_OCUP', 'EDAD', 'ITF', 'GDECCFR'],
        'criterio': 'completitud',   # Ordenado por el % de completitud
        'orden': 'B',               
        'umbral': 60.0               #Columnas con porcentaje mayor o igual a 60
    },
    'analista': {
        'columnas': ['ANO4', 'TRIMESTRE', 'ITF', 'GDECCFR', 'MAS_500'],
        'criterio': 'completitud',   
        'orden': 'A',                
        'umbral': 50.0              
    }
}