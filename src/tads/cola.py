from src.tads import ListaEnlazada
from src.excepciones import ColaVaciaError

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""

    def __init__(self):
        self.__items = ListaEnlazada()
    
    def __str__(self) -> str:
        return str(self.__items)

    def encolar(self, dato):
        self.__items.insertar_al_final(dato)

    def desencolar(self):
        if self.__items.esta_vacia():
            raise ColaVaciaError('Cola vacia')

        dato = self.__items.header._elem
        self.__items.eliminar(dato)
        return dato

    def ver_frente(self):
        if self.__items.esta_vacia():
            raise ColaVaciaError('Cola vacia')

        return self.__items.header._elem

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