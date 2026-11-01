from .busqueda import *
from .ordenamiento import *
import time

def test_time(func, *args):
    start = time.perf_counter()
    resultado = func(*args)
    end = time.perf_counter()
    print(f'Funcion "{func.__name__}" terminada en: {end - start:.6f}s')
    return resultado


if __name__ == "__main__":
    from src.dominio import Biblioteca
    import random

    lista = Biblioteca()._canciones

    lista = lista.shuffle()
    t= lista.tamanio
    k= random.randint(1, t)

    # Prueba busqueda lineal:
    test_time(busqueda_lineal, lista, k)

    # Prueba busqueda binaria
    lista = ordenar_seleccion(lista)
    test_time(busqueda_binaria, lista, k)

    # Prueba ordenar seleccion
    lista = lista.shuffle()
    test_time(ordenar_seleccion, lista)
    # Prueba ordenar insercion
    lista = lista.shuffle()
    test_time(ordenar_insercion, lista)

    # Prueba agrandando biblioteca:

    print("Anterior size:")
    print(lista.tamanio)
    for i in range(2):
        lista += lista.shuffle()
    
    lista = lista.shuffle()
    print("Nuevo size:")
    print(lista.tamanio)

    # Prueba busqueda lineal:
    test_time(busqueda_lineal, lista, k)

    # Prueba busqueda binaria
    lista = ordenar_seleccion(lista)
    test_time(busqueda_binaria, lista, k)

    # Prueba ordenar seleccion
    lista = lista.shuffle()
    test_time(ordenar_seleccion, lista)
    # Prueba ordenar insercion
    lista = lista.shuffle()
    test_time(ordenar_insercion, lista)
