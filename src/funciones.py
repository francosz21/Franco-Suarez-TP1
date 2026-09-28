def informar(columnas, roles, rol=None):
    """
    Genera un informe detallado sobre las columnas configuradas.

    Parámetros:
    columnas : dict
        Diccionario con las columnas como clave y tuplas (tipo, completitud) como valor.
    roles : dict
        Diccionario con las configuraciones por rol.
    rol : str, opcional
        Nombre del rol a consultar. Si es None, muestra todas las columnas
        ordenadas por porcentaje de completitud descendente.
    """
    if rol is None:
        columnas_totales = list(columnas.items())
        columnas_ordenadas = sorted(
            columnas_totales,
            key=lambda c: c[1][1],
            reverse=True
        )
        print("\n--- Informe de todas las columnas (Completitud Descendente) ---")
        for nombre, datos in columnas_ordenadas:
            print(f"Columna: {nombre} | Tipo: {datos[0]} | Completitud: {datos[1]}%")
        return

    if rol not in roles:
        print(f"Error: El rol '{rol}' no existe en la configuración.")
        return

    config_rol = roles[rol]
    cols_interes = config_rol['columnas']
    umbral = config_rol['umbral']

    #  filter()
    columnas_existentes = filter(lambda item: item[0] in cols_interes, columnas.items())
    
    if umbral is not None:
        columnas_filtradas = list(filter(lambda item: item[1][1] >= umbral, columnas_existentes))
    else:
        columnas_filtradas = list(columnas_existentes)

    # Criterio de ordenamiento
    criterio = config_rol.get('criterio', 'completitud')
    es_descendente = config_rol.get('orden', 'A') == 'B'

    if criterio == 'nombre':
        key_func = lambda item: item[0]
    elif criterio == 'completitud':
        key_func = lambda item: item[1][1]
    else:
        print(f"Criterio '{criterio}' no reconocido. Se usará 'completitud' por defecto.")
        key_func = lambda item: item[1][1]

    columnas_ordenadas = sorted(
        columnas_filtradas,
        key=key_func,
        reverse=es_descendente
    )

    # Impresión del resultado
    print(f"\n--- Informe del rol: {rol} ---")
    for nombre, datos in columnas_ordenadas:
        print(f"Columna: {nombre} | Tipo: {datos[0]} | Completitud: {datos[1]}%")