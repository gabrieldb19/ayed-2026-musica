from src.tads import Pila, Cola
from src.excepciones import PilaVaciaError, ColaVaciaError

class Playlist:
    def __init__(self) -> None:
        self._playlist = Cola()
        self._historial = Pila()

    def ver_playlist(self):
        if self._playlist.esta_vacia():
            print("Playlist vacia.")
        else:
            [print(c) for c in self._playlist.items]

    def agregar_playlist(self, cancion):
        self._playlist.encolar(cancion)
        print("> Cancion agregada a la playlist")

    def next_cancion(self):
        try:
            cancion = self._playlist.desencolar()
            print(f"Reproduciendo: {cancion}")
            self._historial.apilar(cancion)
        except ColaVaciaError as e:
            print(e)

    def ver_historial(self):
        if self._historial.esta_vacia():
            print("Historial vacio.")
        else:
            [print(c) for c in list(self._historial.items)[::-1]]

    def ultimo(self):
        try:
            cancion = self._historial.desapilar()
            print(f"Ultima cancion quitada: {cancion}")
        except PilaVaciaError as e:
            print(e)