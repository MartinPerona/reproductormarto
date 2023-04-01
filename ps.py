pip install spotipy
from spotipy.oauth2 import SpotifyOAuth


import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configurar las credenciales de autenticación
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='1dee9e8aeb1248d6975ee41d6c309a3e', client_secret='9bbc05be44dc413f9f24b712e40c05dc', redirect_uri='http://localhost:8888/callback'))

# Buscar una canción por su título
resultados_busqueda = sp.search(q='París', type='track')

# Obtener la URI de la primera canción encontrada
uri_cancion = resultados_busqueda['tracks']['items'][0]['uri']


print(uri_cancion)
# Reproducir la canción
#sp.start_playback(uris=[uri_cancion])
