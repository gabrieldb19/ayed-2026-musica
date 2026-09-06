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

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
