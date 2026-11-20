# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca musical
- Por qué lo eligieron (5–8 líneas): Elegimos el tema de la biblioteca de música por interés en la temática musical. Además, la estructura de un catálogo musical permite modelar y manipular múltiples atributos complejos, como géneros, datos de artistas, duraciones, etc.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```text
- Un ítem del catálogo suele ser una estructura de datos que representa una canción identificada de forma única y que agrupa sus atributos (título, artista, duración, etc.).
- De esta entrega lo unico inmutable es la lista de canciones 'DUMMY' en 'src/dominio/canciones.py'. Por el momento no hay nada mutable hasta aplicar las proximas funcionalidades.
- La colección principal almacena las canciones seleccionadas por el usuario tomando como referencia los datos del catálogo (repositorio global). Sobre esa colección se operan la cola, que gestiona las canciones pendientes a reproducirse en el orden en que fueron agregadas, y la pila, que guarda el historial de reproducción reciente para permitir volver a las canciones escuchadas previamente.
```

## 3. Recursión (E2)

- Función: Biblioteca.versiones_de(id_cancion, pre)
- Caso base: Si no hay versiones simplemente 'return' para terminar esa llamada.
- Caso recursivo: Itera por las diferentes versiones llamando nuevamente a si misma -> versiones_de(v, f'{pre}-'). El argumento 'pre' es un prefijo para mostrar las sub canciones tabuladas. Ej:
    ```
    Cancion_original
    -Subcancion1
    --Subsubcancion1
    -Subcancion2
    ```
- Traza para cancion ID = 1: segun versiones.csv, 1 -> 62

Llamada 1: 
    versiones_de(id_canciones = 1, pre = '') -> buscar(id_canciones = 1, pre = '') Muestra, si existe, la cancion -> buscar_versiones(id_cancion) = [62] -> itera por la lista de versiones llamando a versiones_de(id_canciones = 62, pre = f'{pre}-')

Llamada 2:
    versiones_de(id_canciones = 1, pre = '-') -> buscar(id_canciones = 1, pre = '-') Muestra, si existe, la cancion -> buscar_versiones(id_cancion) = [None] -> return

Output:
```
=== Biblioteca musical — AyED C2 2026 ===
1. Listar catálogo
2. Ver detalle
3. Buscar
4. Ordenar
5. Operación recursiva
6. Colección principal (equipo / menú / playlist)
7. Historial (pila)
8. Cola
9. Guardar / cargar archivos
0. Salir
> 5
ID: 1
[1] De Musica Ligera - Soda Stereo (1990)
-[62] De Musica Ligera (Unplugged) - Soda Stereo (1996)
```


## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | insertar_al_inicio(), insertar_al_final(), eliminar(), buscar(), property: tamanio | esta_vacia() |
| Pila | apilar(), desapilar(), ver_tope(), property: items | esta_vacia() |
| Cola | encolar(), desencolar(), ver_frente(), property: items | esta_vacia() |

ListaEnlazada: Se usar en la clase Biblioteca para almacenar las canciones de la misma.

Pila y Cola: Ambos se usan en la clase Playlist para representar la lista de canciones a reproducir y el historial reproducido.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | O(n) |O(n) | El iterador recorre cada nodo una vez. |
| Ver detalle por id | O(n) mejor caso O(1)| O(1)|	Hace una búsqueda lineal sobre la lista enlazada.|
| Búsqueda lineal | O(n) peor / O(1) mejor | O(1) | Compara elemento a elemento hasta encontrarlo o llegar al final. |
| Búsqueda binaria (sobre list) | O(log n)| O(1) | Cada comparación descarta la mitad del rango. |
| Búsqueda binaria desde ListaEnlazada | O(n) | O(n) | Convertir a list cuesta O(n) y domina sobre las log n comparaciones. |
| Ordenar por selección | O(n²) siempre | O(1) | Dos bucles anidados: n + (n−1) + … + 1 ≈ n²/2 comparaciones, esté o no ordenado. |
| Ordenar por inserción | O(n) mejor / O(n²) peor y promedio | O(1) | Si ya está ordenado hace 1 comparación por elemento; si está al revés, desplaza todo. |
| Ordenar el catálogo (menú) | O(n²) | O(n) | Se pasa a list (O(n)), se ordena y se reconstruye la lista enlazada (O(n)). |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
| búsqueda lineal (list, original) | 67 | 0.000004 |
| búsqueda binaria (list, original) | 67 | 0.000001 |
| búsqueda binaria (ListaEnlazada, original) | 67 | 0.000011 |
| orden selección aleatorio (original) | 67 | 0.000245 |
| orden inserción aleatorio (original) | 67 | 0.000123 |
| orden selección ya ordenado (original) | 67 | 0.000284 |
| orden inserción ya ordenado (original) | 67 | 0.000015 |
| búsqueda lineal (list, x10) | 670 | 0.000035 |
| búsqueda binaria (list, x10) | 670 | 0.000001 |
| búsqueda binaria (ListaEnlazada, x10) | 670 | 0.000087 |
| orden selección aleatorio (x10) | 670 | 0.025126 |
| orden inserción aleatorio (x10) | 670 | 0.012445 |
| orden selección ya ordenado (x10) | 670 | 0.026126 |
| orden inserción ya ordenado (x10) | 670 | 0.000101 |

- Selección estable: False
- Inserción estable: True

*Formma de medicion: clave inexistente como peor caso y repeticiones promediadas*

## 6. Persistencia (E5)

- Formato de texto: se usa CSV (`data/playlist.csv`, `data/historial.csv`) con encabezado en la primera línea, un registro por línea y coma como separador, leído con el módulo `csv`. Es acceso secuencial: se guarda y se carga el archivo completo.
- Layout del registro binario: `struct.Struct("<I 30s 40s 30s 12s 2H")` = 120 bytes por registro.
  id (I, 4 B), título (30 B), artista (40 B), álbum (30 B), género (12 B), año (H, 2 B), duración en segundos (H, 2 B).
  Las cadenas se codifican en UTF-8 y se recortan o rellenan con `\x00` hasta el ancho fijo.
- Header: `struct.Struct("<4s 1s I")` = 9 bytes: magia `AYED`, tema `M` (música) y cantidad de registros.
- Archivos: `data/playlist.bin` y `data/historial.bin`. No se versionan (`*.bin` en `.gitignore`); el programa los genera desde el menú.
- Actualización por posición: `seek(HEADER.size + posicion * FORMATO.size)` y se pisa ese único registro (acceso directo, O(1)). Ej.: el registro 7 empieza en el byte 9 + 7 × 120 = 849. La posición se valida contra la cantidad del header.
- Alta y baja: se hacen sobre la memoria (cola/pila) y se persisten reescribiendo el archivo completo con `guardar_binario`; solo la modificación usa acceso directo.
- Errores: `ArchivoInvalidoError` ante binario truncado, magia incorrecta o tema distinto.
- Limitaciones: los cambios en memoria se persisten recién al elegir "Guardar"; las rutas son relativas a la raíz del repo.

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
| Gabriel Banda | Diseño general, TADs (ListaEnlazada, Pila, Cola), recursión (versiones_de), persistencia CSV y binario, integración del menú. | binario.py, lista_enlazada.py, biblioteca.py |
| Matías Sanguinetti | Algoritmos de búsqueda y ordenamiento. | busqueda.py, ordenamiento.py |
| Areli Rojas | Redacción y revisión de informes, declaracion IA y protocolos de prueba. | PROTOCOLO_PRUEBAS.md, pila.py y cola.py |
