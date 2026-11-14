import csv

def cargar_csv(ruta):
    """Carga secuencial. Devuelve una lista de dicts (E1 puede quedar así)."""
    with open(ruta, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [dict(fila) for fila in reader]


def guardar_csv(ruta, filas, encabezados):
    with open(ruta, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= encabezados)

        writer.writeheader()
        writer.writerows(filas)
