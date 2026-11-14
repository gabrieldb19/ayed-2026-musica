import datetime
from src.dominio.canciones import Cancion
from src.persistencia.texto import cargar_csv
from src.tads import ListaEnlazada
from src.excepciones import ItemNoEncontradoError
from src.algoritmos import busqueda_lineal, busqueda_binaria, ordenar_insercion
from src.algoritmos.ordenamiento import ordenar_insercion

CLAVES = {
    "id": lambda c: c.id,
    "titulo": lambda c: c.titulo.lower(),
    "artista": lambda c: c.artista.lower(),
    "anio": lambda c: c.anio,
    "duracion": lambda c: c.duracion_seg,
}

class Biblioteca:
    def __init__(self, ruta_canciones='data/canciones.csv', ruta_versiones='data/versiones.csv') -> None:
        self._canciones = ListaEnlazada()
        self._versiones = cargar_csv(ruta_versiones)

        for fila in cargar_csv(ruta_canciones):
            self._canciones.insertar_al_final(Cancion(**fila))

        self._orden = "id"


    def listar(self):
        print(self._canciones)

    def buscar(self, id_cancion):
        id_cancion = int(id_cancion)
        for c in self._canciones:
            if c.id == id_cancion:
                return c
        else:   raise ItemNoEncontradoError("# Cancion no encontrada")

    def ver_detalle(self, id_cancion, pre= ''):
        """Devuelve la Cancion con ese id."""
        try:
            cancion = self.buscar(id_cancion)
            print(f'{pre}{cancion.titulo} - {cancion.artista} - {cancion.album} - {cancion.genero} - {cancion.anio} ({str(datetime.timedelta(seconds=cancion.duracion_seg))})')
        except ItemNoEncontradoError as e:
            print(e)

    def buscar_versiones(self, id_cancion):
        """IDs de las canciones que son versión (cover/live/remix) directa de id_cancion."""
        return [
            fila['cancion_id']
            for fila in self._versiones
            if fila['version_de_id'] == id_cancion
        ]

    def versiones_de(self, id_cancion, pre= ''):
        self.ver_detalle(id_cancion, pre)

        versiones = self.buscar_versiones(id_cancion)

        if not versiones:
            return
        
        for v in versiones:
            self.versiones_de(v, f'{pre}-')

    def _normalizar(self, campo, valor):
        return int(valor) if campo == "id" else valor.strip().lower()

    def ordenar(self, algoritmo, campo):
        datos = list(self._canciones)              # O(n)
        algoritmo(datos, CLAVES[campo])            # O(n²) / O(n) mejor caso
        nueva = ListaEnlazada()
        for c in reversed(datos):                  # O(n) (insertar_al_final sería O(n²))
            nueva.insertar_al_inicio(c)
        self._canciones = nueva
        self._orden = campo

    def buscar_lineal(self, campo, valor):
        try:
            clave = self._normalizar(campo, valor)
        except ValueError:
            print("# El ID debe ser un número")
            return None
        return busqueda_lineal(self._canciones, clave, CLAVES[campo])

    def buscar_binaria(self, campo, valor):
        try:
            clave = self._normalizar(campo, valor)
        except ValueError:
            print("# El ID debe ser un número")
            return None
        if self._orden != campo:
            print(f"Catálogo ordenado por {campo} (inserción); usando búsqueda binaria.")
            self.ordenar(ordenar_insercion, campo)
        return busqueda_binaria(list(self._canciones), clave, CLAVES[campo])