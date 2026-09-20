from src.dominio.canciones import Cancion
from src.persistencia.texto import cargar_csv

class Biblioteca:
    def __init__(self, ruta_canciones='data/canciones.csv', ruta_versiones='data/versiones.csv') -> None:
        self._canciones = [Cancion(**fila) for fila in cargar_csv(ruta_canciones)]
        self._versiones = cargar_csv(ruta_versiones)


    def listar(self):
        for cancion in self._canciones:
            print(cancion)

    def buscar(self, id_cancion, pre= ''):
        """Devuelve la Cancion con ese id."""
        id_cancion = int(id_cancion)
        for c in self._canciones:
            if c.id == id_cancion:
                return print(f'{pre}{c}')
        return print(f'No existe la cancion id: {id_cancion}')

    def buscar_versiones(self, id_cancion):
        """IDs de las canciones que son versión (cover/live/remix) directa de id_cancion."""
        return [
            fila['cancion_id']
            for fila in self._versiones
            if fila['version_de_id'] == id_cancion
        ]

    def versiones_de(self, id_cancion, pre= ''):
        self.buscar(id_cancion, pre)

        versiones = self.buscar_versiones(id_cancion)

        if not versiones:
            return
        
        for v in versiones:
            self.versiones_de(v, f'{pre}-')