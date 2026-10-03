from src.tads.nodo import Nodo

class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""
    class IteradorLista:
        def __init__(self, cabeza):
            self.actual = cabeza

        def __iter__(self):
            return self

        def __next__(self):
            if self.actual is None:
                raise StopIteration
            elemento = self.actual._elem
            self.actual = self.actual._nxt
            return elemento


    def __init__(self):
        self.header = None
        self.__tamanio = 0

    def __str__(self):
        return str(list(self))
    
    def __iter__(self):
        return self.IteradorLista(self.header)


    def esta_vacia(self) -> bool:
        return False if self.header else True

    def insertar_al_inicio(self, dato) -> None:
        nodo = Nodo(dato)
        nodo._nxt = self.header
        self.header = nodo
        self.__tamanio += 1

    def insertar_al_final(self, dato) -> None:
        if not self.header:
            self.header = Nodo(dato)
            return
        
        n = self.header
        while n._nxt:
            n = n._nxt

        n._nxt = Nodo(dato)
        self.__tamanio += 1

    def insertar_ordenado(self, dato, clave):
        raise NotImplementedError #TODO Implementar prox...

    def eliminar(self, dato) -> bool:
        anterior = None
        actual = self.header

        while actual:
            if actual._elem == dato:
                if anterior is None:
                    self.header = actual._nxt
                else:
                    anterior._nxt = actual._nxt
                self.__tamanio -= 1
                return True
            
            anterior = actual
            actual = actual._nxt

        return False

    def buscar(self, dato):
        actual = self.header

        while actual:
            if actual._elem == dato:
                return actual._elem
            actual = actual._nxt
        
        return None


    @property
    def tamanio(self):
        return self.__tamanio
