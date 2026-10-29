from src.excepciones import ItemNoEncontradoError

def busqueda_lineal(coleccion, clave): 
    """Devuelve el elemento cuya clave es igual a 'clave', o None si no existe. 
    """
    try:
        clave = int(clave)
        for elemento in coleccion: 
            if elemento.id == clave: 
                return elemento
        else: raise ItemNoEncontradoError("# Cancion no encontrada")
    except Exception as e:
        print(e)


def busqueda_binaria(coleccion, clave): 
    """Búsqueda binaria. REQUIERE que la colección esté ordenada por esa 
    clave.""" 
    izq = 0 
    der = len(coleccion) - 1 
    while izq <= der:
        medio = (izq + der) // 2 
        valor = coleccion[medio]
        if valor.id == clave: 
            return coleccion[medio] 
        elif valor.id < clave: 
            izq = medio + 1
        else:
            der = medio - 1
    return None 
