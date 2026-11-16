from src.tads import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
    """TAD pila implementado sobre ListaEnlazada."""

    def __init__(self):
        self.__items = ListaEnlazada()

    def __str__(self) -> str:
        return str(self.__items)

    def apilar(self, dato):
        self.__items.insertar_al_final(dato)

    def desapilar(self):
        self.ver_tope()
        return self.__items.eliminar_ultimo()

    def ver_tope(self):
        if self.__items.esta_vacia():
            raise PilaVaciaError('Pila vacia')

        for dato in self.__items:
            tope = dato
        return tope

    def esta_vacia(self):
        return self.__items.esta_vacia()

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, lista):
        if isinstance(lista, ListaEnlazada):
            self.__items = lista
        else:
            raise TypeError("El objeto a asignar en Cola.items debe ser una instancia de ListaEnlazada")