"""Registros de longitud fija con struct.

Layout sugerido (documentar el definitivo en docs/INFORME.md):

Header:
  magia     4s   b'AYED'
  tema      1s   b'P' | b'R' | b'M'
  cantidad  I    unsigned int

El registro depende del tema. Ejemplo Pokédex:
  id          I
  nombre     20s
  tipo1      12s
  tipo2      12s
  hp          H
  ataque      H
  defensa     H
  velocidad   H
  generacion  H
"""
import struct
from src.tads import ListaEnlazada
from src.dominio.canciones import Cancion
from src.excepciones import ArchivoInvalidoError

FORMATO = struct.Struct("<I 30s 40s 30s 12s 2H")
HEADER = struct.Struct("<4s 1s I")
MAGIA = b'AYED'
TEMA = b"M"


def _a_bytes(texto, ancho):
    return texto.encode("utf-8")[:ancho].ljust(ancho, b"\x00")

def _a_texto(datos):
    return datos.rstrip(b"\x00").decode("utf-8")

def _item_a_tupla(c: Cancion):
    """Objeto del dominio → tupla lista para FORMATO.pack. AJUSTÁ A TU TEMA."""
    return (
        c.id,
        _a_bytes(c.titulo, 30),
        _a_bytes(c.artista, 40),
        _a_bytes(c.album, 30),
        _a_bytes(c.genero, 12),
        c.anio,
        c.duracion_seg,
    )

def _tupla_a_item(t):
    """Tupla que salió de FORMATO.unpack → objeto del dominio. AJUSTÁ A TU TEMA."""
    return Cancion(
                    id= t[0],
                    titulo= _a_texto(t[1]),
                    artista= _a_texto(t[2]),
                    album= _a_texto(t[3]),
                    genero= _a_texto(t[4]),
                    anio= t[5],
                    duracion_seg= t[6]
                    )


def guardar_binario(ruta, items):
    with open(ruta, mode='wb') as binfile:
        binfile.write(HEADER.pack(MAGIA, TEMA, items.tamanio))

        packlist = []
        for item in items:
            packlist.append(FORMATO.pack(*_item_a_tupla(item)))
        
        binfile.writelines(packlist)


def cargar_binario(ruta):
    with open(ruta, mode='rb') as binfile:
        header = binfile.read(HEADER.size)
        if len(header) < HEADER.size:
            raise ArchivoInvalidoError("Binario truncado: ni siquiera tiene header completo.")
        magia, tema, cantidad = HEADER.unpack(header)
        if magia != b"AYED":
            raise ArchivoInvalidoError("Magia incorrecta: este archivo no es de este TP.")
        if tema != TEMA:
            raise ArchivoInvalidoError(f"El tema del archivo ({tema!r}) no es el mío ({TEMA!r}).")
        
        catalogo = ListaEnlazada()
        for _ in range(cantidad):
            datos = binfile.read(FORMATO.size)
            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError(
                    "Binario truncado: el header dice más registros de los que hay."
                )
            catalogo.insertar_al_final(_tupla_a_item(FORMATO.unpack(datos)))
        return catalogo


def actualizar_registro(ruta, posicion, item):
    """Pisa un registro por posición (acceso directo). posicion es 0-based."""
    if not isinstance(posicion, int):
        raise TypeError("La posicion debe ser un entero")
    if not isinstance(item, Cancion):
        raise TypeError("El el objeto debe ser una instancia de Cancion")
    
    with open(ruta, "r+b") as archivo:
        cabecera = archivo.read(HEADER.size)
        cantidad = HEADER.unpack(cabecera)[2]
        if not 0 <= posicion < cantidad:
            raise IndexError(f"Posición {posicion} fuera de rango (0-{cantidad - 1})")
        archivo.seek(HEADER.size + posicion * FORMATO.size)
        archivo.write(FORMATO.pack(*_item_a_tupla(item)))
