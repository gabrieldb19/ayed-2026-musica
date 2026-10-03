from src.tads import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
    """TAD pila implementado sobre ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()

    def __str__(self) -> str:
        return str(self._items)

    def apilar(self, dato):
        self._items.insertar_al_final(dato)

    def desapilar(self):
        if self._items.esta_vacia():
            raise PilaVaciaError('Vacia la wea')

        n = 0
        for dato in self._items:
            if n == self._items.tamanio:
                resultado = dato
                self._items.eliminar(dato)
                return resultado
            n += 1

    def ver_tope(self):
        if self._items.esta_vacia():
            raise PilaVaciaError('Vacia la wea')

        n = 0
        for dato in self._items:
            if n == self._items.tamanio:
                return dato
            n += 1

    def esta_vacia(self):
        return self._items.esta_vacia()