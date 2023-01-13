# -*- coding: utf-8 -*-

# se não tiver spotipy instalado, rode o comando abaixo no terminal
# pip install spotipy --upgrade

import spotipy

sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyOAuth(
        client_id='3a92f783c17f4b95bc75d536dc51be3d',
        client_secret='89e6b1f4d2914d158a34c71f71190d2f',
        redirect_uri="https://localhost:8000/callback",
        scope="user-library-read playlist-modify-public user-library-modify playlist-modify-private"
        )
    )
sp.current_user_saved_tracks() 
# vai te redirecionar para uma tela de login do spotify. copia o link depois de logar e cola aqui


# https://localhost:8000/callback?code=AQBzza3sG5CejY4YC10EZ-Kg3YvujKbBCFQJHuwyT0qfPybxB8u9xQe2EY4O7jfId9e1DX0ueT-ihQMXObZXzX9qXxtAjprdSrmt0VG4_VAvVZrYeFlGsfqht-jcE7gm2p5zOxQyRNFqOcGpZ3n7FV1BBQ1Jvh3FbaQSQXwqs4D62LYd5qK



def searchArtist(name):
  # buscar um artista por nome -> nome indiferente a letras maiúsculas e minúsculas, mas tem que estar escrito certo, inclusive acentos
  res = sp.search(name,limit=10)
  for i in range(10): # testa os 10 primeiros artistas
    artist = res['tracks']['items'][i]['album']['artists'][0]
    if name.lower() == artist['name'].lower():
      return artist['id']
  print('ERRO: artista achado:'+res['tracks']['items'][0]['album']['artists'][0]['name'])
  return -1

def searchTrack(name,artist=''):
   # buscar uma música por nome -> nome indiferente a letras maiúsculas e minúsculas, mas tem que estar escrito certo, inclusive acentos
  stringSearch = name+' '+artist+' &type=track'
  rec = sp.search(stringSearch,limit=10)
  for i in range(10):
    track = rec['tracks']['items'][i]
    trackBool = track['name'].lower() == name.lower() 
    artistBool = track['artists'][0]['name'].lower() == artist.lower()
    if (trackBool and artistBool) or (artist=='' and trackBool):
      return track['id']
  track = rec['tracks']['items'][0]
  print('ERRO: track achada:'+track['name'])
  print('ERRO: artista achado:'+track['artists'][0]['name'])
  return -1

def auxTrackSearch(item: list):
  # função auxiliar para usar com map()
  if len(item) == 1:
    item.append('')
  return searchTrack(item[0],item[1])

def recommentationsToPlaylist(rec,name,description=''):
  # pega os resultados de um retorno da função sp.recommendations() e salva numa playlist
  playlist = sp.user_playlist_create(sp.me()['id'],name=name,description=description)
  listTracks = []
  for item in rec['tracks']:
    listTracks.append(item['id'])
  sp.playlist_add_items(playlist['id'],listTracks)
  print('=================================== \n playlist ',name,' criada com sucesso.')

def recommendTracks(listMusics=[], listArtists=[], createPlaylist=False, name='', playlist_size=20):
  # list tracks no formato [['passionfruit', 'drake'],['aquela fé','don l']]
  # list artists no formato ['frank ocean', 'nill']
  # tamanho das duas listas somados pode ser até 5
  if listMusics == [] and listArtists ==[]:
    print('listas vazias')
    return
  if len(listMusics) + len(listArtists) > 5:
    print('maximo de musicas+artistas é 5')
    return
  listIdsMusics = list(map(auxTrackSearch,listMusics))
  listIdsArtists = list(map(searchArtist,listArtists))
  if -1 in listIdsMusics: 
    print('problema na track '+str(listMusics[listIdsMusics.index(-1)]))
    print(listIdsMusics)
    return
  if -1 in listIdsArtists: 
    print('problema no artista '+listArtists[listIdsArtists.index(-1)])
    print(listIdsArtists)
    return
  rec = sp.recommendations(seed_artists=listIdsArtists, seed_tracks=listIdsMusics, limit=playlist_size)
  print('_________ PLAYLIST __________')
  for item in rec['tracks']:
    print(item['name'],' --- ',item['artists'][0]['name'])
  print('____________________________')
  if createPlaylist:
    if name == '':
      name = 'playlist baseada nas musicas '+str(listMusics)[1:-1]+'e nos artistas'+str(listArtists)[1:-1]
    description = description='playlist baseada nas musicas '+str(listMusics)[1:-1]+'e nos artistas'+str(listArtists)[1:-1]
    recommentationsToPlaylist(rec,name,description)
  return rec

def main():
  #testes
  rec = recommendTracks(
      listMusics=[['Passionfruit', 'Drake'],['aquela fé','don l']],
      listArtists=['Nill','Don L','Makalister']
  )
  # recommentationsToPlaylist(rec,'nome da playlist.') # roda se quiser criar uma playlist


# main()