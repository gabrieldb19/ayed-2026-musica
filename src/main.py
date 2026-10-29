from src.config import TEMA
from src.dominio import BIBLIOTECA, PLAYLIST
from src.decor import opcion
from src.algoritmos import *

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
menu = ["", 
        f"=== {nombre} — AyED C2 2026 ===", 
        "1. Listar catálogo", 
        "2. Ver detalle", 
        "3. Buscar/Ordenar", 
        "4. Operación recursiva", 
        "5. Playlist (mostrar opciones)", 
        "6. Guardar / cargar archivos", 
        "0. Salir"]

sub_playlist = ["=== Playlist ===",
        "6.1. Mostrar playlist",
        "6.2. Agregar a playlist",
        "6.3. Playlist (next)",
        "6.4. Mostrar historial",
        "6.5. Historial (quitar)",
        "0. Volver al menu principal"]

sub_bo = ["=== Busqueda - Ordenamiento ===",
        "3.1. Busqueda Lineal",
        "3.2. Busqueda Binaria",
        "3.3. Ordenar por Seleccion",
        "3.4. Ordenar por Insercion",
        "0. Volver al menu principal"]

menu = "\n".join(menu)
sub = "\n".join(sub_playlist)
bo = "\n".join(sub_bo)

@opcion(msg= bo)
def bo_menu_match(opcion= None):
    match opcion:
        case 0:
            return False
        case 1:
            id_ = input("ID: ").strip()
            cancion = busqueda_lineal(BIBLIOTECA._canciones, id_)
            if cancion:
                print(cancion)
        case 2:
            pendiente()
        case 3:
            pendiente()
        case 4:
            pendiente()
        case _:
            print("Opción inválida.")
    
    return True

@opcion(msg= sub)
def sub_menu_match(opcion= None):
    match opcion:
        case 0:
            return False
        case 1:
            PLAYLIST.ver_playlist()
        case 2:
            id_ = input("ID: ").strip()
            cancion = BIBLIOTECA.buscar(id_)
            if cancion:
                PLAYLIST.agregar_playlist(cancion)
        case 3:
            PLAYLIST.next_cancion()
        case 4:
            PLAYLIST.ver_historial()
        case 5:
            PLAYLIST.ultimo()
        case _:
            print("Opción inválida.")
    
    return True

@opcion(msg= menu)
def menu_match(opcion= None):
    match opcion:
        case 0:
            print("Chau.")
            return False
        case 1:
            BIBLIOTECA.listar()
        case 2:
            id_ = input('ID: ')
            BIBLIOTECA.ver_detalle(id_)
        case 3:
            bo_menu()
        case 4:
            BIBLIOTECA.versiones_de(input('ID: '))
        case 5:
            sub_menu()
        case 6:
            pendiente()
        case _:
            print("Opción inválida.")
    
    return True

def bo_menu():
    continuar = True
    while continuar:
        continuar = bo_menu_match()

def sub_menu():
    continuar = True
    while continuar:
        continuar = sub_menu_match()

def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    continuar = True
    while continuar:
        continuar = menu_match()


if __name__ == "__main__":
    main()
