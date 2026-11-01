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
        tope = self.ver_tope()
        self.__items.eliminar(tope)
        return tope

    def ver_tope(self):
        if self.__items.esta_vacia():
            raise PilaVaciaError('Vacia la wea')

        for dato in self.__items:
            tope = dato
        return tope

    def esta_vacia(self):
        return self.__items.esta_vacia()

    @property
    def items(self):
        return self.__items