from src.config import TEMA
from src.dominio import BIBLIOTECA, PLAYLIST
from src.decor import opcion

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
        "3. Buscar", 
        "4. Ordenar", 
        "5. Operación recursiva", 
        "6. Playlist (mostrar opciones)", 
        "7. Guardar / cargar archivos", 
        "0. Salir"]

sub = ["=== Playlist ===",
        "6.1. Mostrar playlist",
        "6.2. Agregar a playlist",
        "6.3. Playlist (next)",
        "6.4. Mostrar historial",
        "6.5. Historial (quitar)",
        "0. Volver al menu principal"]

menu = "\n".join(menu)
sub = "\n".join(sub)

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
            BIBLIOTECA.ver_detalle(input('ID: '))
        case 3:
            print(BIBLIOTECA.buscar(input('ID: '))) #TODO ---> Solucion temporal
        case 5:
            BIBLIOTECA.versiones_de(input('ID: '))
        case 6:
            sub_menu()
        case 4|7:
            pendiente()
        case _:
            print("Opción inválida.")
    
    return True


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
