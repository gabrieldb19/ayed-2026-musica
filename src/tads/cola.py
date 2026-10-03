from src.tads import ListaEnlazada
from src.excepciones import PilaVaciaError

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()
    
    def __str__(self) -> str:
        return str(self._items)

    def encolar(self, dato):
        self._items.insertar_al_final(dato)

    def desencolar(self):
        if self._items.esta_vacia():
            raise PilaVaciaError('Vacia la wea')

        dato = self._items.header._elem
        self._items.eliminar(dato)
        return dato

    def ver_frente(self):
        if self._items.esta_vacia():
            raise PilaVaciaError('Vacia la wea')

        return self._items.header._elem

    def esta_vacia(self):
        return self._items.esta_vacia()