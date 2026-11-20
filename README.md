# AyED C2 2026 — Biblioteca musical — Grupo 33

## Integrantes

| Nombre | Mail | GitHub |
| --- | --- | --- |
| Banda Gabriel | gabriel.d.banda@gmail.com | https://github.com/gabrieldb19 |
| Rojas Areli | arelirojas380@gmail.com | https://github.com/Areli1233 |
| Sanguinetti Matias | mtssanguinetti@gmail.com | https://github.com/NicolasSangd |

## Cómo ejecutarlo

Requiere Python 3.10 o superior (solo biblioteca estándar, no hay `requirements.txt`).
Desde la **raíz del repo**:

```text
python -m src.main
```

En Windows, si `python` no anda: `py -3 -m src.main`.

Hay que ejecutarlo desde la raíz porque las rutas a `data/` son relativas a esa carpeta.

## Tema

Biblioteca musical: un catálogo de 67 canciones (`data/canciones.csv`) con sus versiones
(cover, live, remix) en `data/versiones.csv`, y una playlist con historial de reproducción.

## Qué hace

Gestor de catálogo por consola. El menú principal agrupa las operaciones en submenús:

| Opción | Operación |
| --- | --- |
| 1 | Listar catálogo (con el iterador de `ListaEnlazada`) |
| 2 | Ver detalle de una canción por id |
| 3 | Buscar / Ordenar |
| 3.1 / 3.2 | Búsqueda lineal / binaria por id o título. La binaria reordena el catálogo y avisa si hace falta |
| 3.3 / 3.4 | Ordenar por selección / inserción, por id, título, artista, año o duración |
| 4 | Operación recursiva: árbol de versiones de una canción (`Biblioteca.versiones_de`) |
| 5 | Playlist: cola de reproducción (agregar, next) e historial (pila: ver, quitar la última) |
| 6 | Guardar / cargar playlist e historial en CSV y en binario con `struct`, y cambiar una canción de la playlist por posición (acceso directo con `seek`) |
| 0 | Salir |

Estructuras propias: `ListaEnlazada`, `Pila` y `Cola` (`src/tads/`).
Algoritmos propios: búsqueda lineal y binaria, ordenamiento por selección y por inserción (`src/algoritmos/`).
Formato binario: header de 9 bytes (magia `AYED`, tema `M`, cantidad) y registros de 120 bytes (detalle en `docs/INFORME.md` §6).

## Estructura del repo

```text
src/dominio/       Cancion, Biblioteca, Playlist
src/tads/          Nodo, ListaEnlazada, Pila, Cola
src/algoritmos/    busqueda.py, ordenamiento.py (y test.py con las mediciones)
src/persistencia/  texto.py (CSV), binario.py (struct)
data/              datasets de la cátedra, playlist.csv e historial.csv
docs/              INFORME.md, PROTOCOLO_PRUEBAS.md, DECLARACION_IA.md
```

## Limitaciones conocidas

- La playlist no tiene tope de tamaño (es una playlist, no un equipo). `ColeccionLlenaError` está definida pero no se usa.
- Solo se persisten la playlist y el historial. El catálogo siempre se arma desde `data/canciones.csv`, y el orden elegido con "Ordenar" vive solo en memoria.
- No hay alta ni baja de canciones del catálogo. El ABM persistente se limita a la playlist (agregar, quitar del historial, cambiar por posición).
- En binario, los textos se recortan al ancho fijo (título 30 B, artista 40 B, álbum 30 B, género 12 B). Un título más largo se corta, y si el corte parte una letra con acento puede fallar la carga.
- Los cambios se guardan solo al elegir "Guardar" en el menú 6.
- La búsqueda binaria por título trabaja sobre una copia en `list` del catálogo (cuesta O(n)), y con títulos repetidos devuelve uno solo de ellos.
- El menú tiene 6 opciones principales con submenús, en lugar de las 10 numeradas de la guía, pero cubre las mismas operaciones.
- El árbol de versiones asume que `versiones.csv` no tiene ciclos.