DUMMY = [
    {'id': 1, 'titulo': 'De Musica Ligera', 'artista': 'Soda Stereo', 'album': 'Cancion Animal', 'genero': 'Rock', 'anio': 1990, 'duracion_seg': 213},
    {'id': 2, 'titulo': 'Persiana Americana', 'artista': 'Soda Stereo', 'album': 'Signos', 'genero': 'Rock', 'anio': 1986, 'duracion_seg': 263},
    {'id': 3, 'titulo': 'En la Ciudad de la Furia', 'artista': 'Soda Stereo', 'album': 'Doble Vida', 'genero': 'Rock', 'anio': 1988, 'duracion_seg': 351},
    {'id': 4, 'titulo': 'Crimen', 'artista': 'Gustavo Cerati', 'album': 'Ahí vamos', 'genero': 'Rock', 'anio': 2006, 'duracion_seg': 239},
]

def listar_canciones():
    for c in DUMMY:
        print(f'Titulo: {c['titulo']} - Autor: {c['artista']}')