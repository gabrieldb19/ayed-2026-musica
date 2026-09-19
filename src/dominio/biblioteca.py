from src.dominio.canciones import Cancion
from src.persistencia.texto import cargar_csv

class Biblioteca:
    def __init__(self, ruta_canciones='data/canciones.csv', ruta_versiones='data/versiones.csv') -> None:
        self._canciones = [Cancion(**fila) for fila in cargar_csv(ruta_canciones)]
        self._versiones = cargar_csv(ruta_versiones)


    def listar(self):
        for cancion in self._canciones:
            print(cancion)

    def buscar(self, id_cancion):
        """Devuelve la Cancion con ese id.

        return -> None | Cancion
        """
        id_cancion = int(id_cancion)
        for c in self._canciones:
            if c.id == id_cancion:
                return c
        return None

    def buscar_versiones(self, id_cancion):
        """IDs de las canciones que son versión (cover/live/remix) directa de id_cancion."""
        return [
            fila['cancion_id']
            for fila in self._versiones
            if fila['version_de_id'] == id_cancion
        ]

    def versiones_de(self, id_cancion):
        versiones_ = self.buscar_versiones(id_cancion)

        if not versiones_:
            return []
        resultados = list(versiones_)

        for v in versiones_:
            resultados.append(self.versiones_de(v))

        print(resultados)