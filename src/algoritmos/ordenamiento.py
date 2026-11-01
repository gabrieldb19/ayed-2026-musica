def ordenar_seleccion(coleccion): 
    """Ordena la colección in place por selección (ascendente).""" 
    n = len(coleccion) 
    for i in range(n): 
        pos_min = i 
        for j in range(i + 1, n): 
            if coleccion[j].id < coleccion[pos_min].id: 
                pos_min = j 
        coleccion[i], coleccion[pos_min] = coleccion[pos_min], coleccion[i] 
    return coleccion 



def ordenar_insercion(coleccion): 
    """Ordena la colección in place por inserción (ascendente).""" 
    for i in range(1, len(coleccion)): 
        actual = coleccion[i] 
        j = i - 1 
        while j >= 0 and coleccion[j].id > actual.id: 
            coleccion[j + 1] = coleccion[j]
            j -= 1 
        coleccion[j + 1] = actual
    return coleccion 