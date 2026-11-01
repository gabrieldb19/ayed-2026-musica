import random
import time
from src.dominio.biblioteca import Biblioteca
from src.tads import ListaEnlazada
from .busqueda import busqueda_lineal, busqueda_binaria
from .ordenamiento import ordenar_seleccion, ordenar_insercion

por_id = lambda c: c.id
REPS = 500


def medir_busqueda(func, coleccion, clave, reps=REPS):
    ini = time.perf_counter()
    for _ in range(reps):
        func(coleccion, clave, por_id)
    return (time.perf_counter() - ini) / reps


def medir_orden(algoritmo, datos, reps=3):
    total = 0.0
    for _ in range(reps):
        copia = list(datos)
        ini = time.perf_counter()
        algoritmo(copia, por_id)
        total += time.perf_counter() - ini
    return total / reps


def a_lista_enlazada(datos):
    nueva = ListaEnlazada()
    for x in reversed(datos):
        nueva.insertar_al_inicio(x)
    return nueva


def es_estable(lista, campo):
    return all(getattr(a, campo) != getattr(b, campo) or a.id < b.id
                for a, b in zip(lista, lista[1:]))


if __name__ == "__main__":
    original = list(Biblioteca()._canciones)
    filas = []

    for etiqueta, datos in (("original", original), ("x10", original * 10)):
        n = len(datos)
        desordenado = list(datos)
        random.shuffle(desordenado)
        ordenado = ordenar_insercion(list(desordenado), por_id)
        enlazada = a_lista_enlazada(ordenado)
        peor = -1  # clave inexistente = peor caso

        filas += [
            (f"búsqueda lineal (list, {etiqueta})", n, medir_busqueda(busqueda_lineal, desordenado, peor)),
            (f"búsqueda binaria (list, {etiqueta})", n, medir_busqueda(busqueda_binaria, ordenado, peor)),
            (f"búsqueda binaria (ListaEnlazada, {etiqueta})", n, medir_busqueda(busqueda_binaria, enlazada, peor, reps=50)),
            (f"orden selección aleatorio ({etiqueta})", n, medir_orden(ordenar_seleccion, desordenado)),
            (f"orden inserción aleatorio ({etiqueta})", n, medir_orden(ordenar_insercion, desordenado)),
            (f"orden selección ya ordenado ({etiqueta})", n, medir_orden(ordenar_seleccion, ordenado)),
            (f"orden inserción ya ordenado ({etiqueta})", n, medir_orden(ordenar_insercion, ordenado)),
        ]

    print("| Operación | n | segundos |\n| --- | --- | --- |")
    for nombre, n, seg in filas:
        print(f"| {nombre} | {n} | {seg:.6f} |")

    # Estabilidad (para el informe): ordenar por género, desempate esperado = id ascendente
    base = list(Biblioteca()._canciones)
    por_genero = lambda c: c.genero
    print("\nSelección estable:", es_estable(ordenar_seleccion(list(base), por_genero), "genero"))
    print("Inserción estable:", es_estable(ordenar_insercion(list(base), por_genero), "genero"))