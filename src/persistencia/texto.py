import csv

def cargar_csv(ruta):
    """Carga secuencial. Devuelve una lista de dicts (E1 puede quedar así)."""
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [dict(fila) for fila in reader]


def guardar_csv(ruta, filas, encabezados):
    raise NotImplementedError
