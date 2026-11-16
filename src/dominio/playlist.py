from src.config import PLAYLIST_PATH, HISTORIAL_PATH, ENCABEZADOS
from src.persistencia import *
from src.dominio.canciones import Cancion
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

    def load_csv(self):
        self._playlist.items = ListaEnlazada()
        for fila in cargar_csv(PLAYLIST_PATH['csv']):
            self._playlist.items.insertar_al_final(Cancion(**fila))

        print(f'> Playlist cargada desde csv: {PLAYLIST_PATH["csv"]}')

        self._historial.items = ListaEnlazada()
        for fila in cargar_csv(HISTORIAL_PATH['csv']):
            self._historial.items.insertar_al_final(Cancion(**fila))

        print(f'> Historial cargado desde csv: {HISTORIAL_PATH["csv"]}')

    def save_csv(self):
        if not self._playlist.items.esta_vacia():
            canciones = []
            for cancion in self._playlist.items:
                c = cancion.to_dict()
                canciones.append(c)

            guardar_csv(ruta=PLAYLIST_PATH['csv'],
                        filas= canciones,
                        encabezados= ENCABEZADOS
                        )

            print(f'> Playlist guardada en: {PLAYLIST_PATH["csv"]}')

        if not self._historial.items.esta_vacia():
            canciones = []
            for cancion in self._historial.items:
                c = cancion.to_dict()
                canciones.append(c)

            guardar_csv(ruta=HISTORIAL_PATH['csv'],
                        filas= canciones,
                        encabezados= ENCABEZADOS
                        )

            print(f'> Historial guardado en: {HISTORIAL_PATH["csv"]}')

    def load_bin(self):
        try:
            lista = cargar_binario(PLAYLIST_PATH['bin'])
            self._playlist.items = lista
            print(f'> Playlist cargada desde: {PLAYLIST_PATH["bin"]}')

            lista = cargar_binario(HISTORIAL_PATH['bin'])
            self._historial.items = lista
            print(f'> Historial cargado desde: {HISTORIAL_PATH["bin"]}')
        except Exception as e:
            print(e)

    def save_bin(self):
        if not self._playlist.items.esta_vacia():
            guardar_binario(PLAYLIST_PATH['bin'], self._playlist.items)
            print(f'> Playlist guardada en: {PLAYLIST_PATH["bin"]}')

        if not self._historial.items.esta_vacia():
            guardar_binario(HISTORIAL_PATH['bin'], self._historial.items)
            print(f'> Historial guardado en: {HISTORIAL_PATH["bin"]}')

    def cambiar_cancion(self, biblioteca):
        try:
            n = int(input('> Posicion: '))
            i = input('> ID nuevo: ')

            nuevo = biblioteca.buscar(i)
            actualizar_registro(PLAYLIST_PATH['bin'], n, nuevo)

            print('Registro actualizado exitosamente!')
            print('Recargando playlist actualizada...')

            self.load_bin()

        except Exception as e:
            print(e)