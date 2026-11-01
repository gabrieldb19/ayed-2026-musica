from src.excepciones import ItemNoEncontradoError

def busqueda_lineal(coleccion, clave): 
    """Busca elemento basado en ID
    - Si no lo encuentra lanza error: ItemNoEncontradoError
    - Si la clave a buscar no es entero, captura y muestra error
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
    try:
        clave = int(clave)
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
        
        raise ItemNoEncontradoError("# Cancion no encontrada")
    except Exception as e:
        print(e)