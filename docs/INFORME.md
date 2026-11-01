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

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
