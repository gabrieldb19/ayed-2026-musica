def busqueda_lineal(coleccion, clave, obtener_clave=None):
    for elemento in coleccion:
        valor = elemento if obtener_clave is None else obtener_clave(elemento)
        if valor == clave:
            return elemento
    return None


def busqueda_binaria(coleccion, clave, obtener_clave):
    """REQUIERE coleccion ordenada por esa clave y con acceso O(1) (list)."""
    izq, der = 0, len(coleccion) - 1
    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave(coleccion[medio])
        if valor == clave:
            return coleccion[medio]
        elif valor < clave:
            izq = medio + 1
        else:
            der = medio - 1
    return None