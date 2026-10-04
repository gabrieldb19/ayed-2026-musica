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
        if self.__items.esta_vacia():
            raise PilaVaciaError('Vacia la wea')

        n = 0
        for dato in self.__items:
            if n == self.__items.tamanio:
                resultado = dato
                self.__items.eliminar(dato)
                return resultado
            n += 1

    def ver_tope(self):
        if self.__items.esta_vacia():
            raise PilaVaciaError('Vacia la wea')

        n = 0
        for dato in self.__items:
            if n == self.__items.tamanio:
                return dato
            n += 1

    def esta_vacia(self):
        return self.__items.esta_vacia()

    @property
    def items(self):
        return self.__items