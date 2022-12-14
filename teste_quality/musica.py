def shuffle_musicas(musicas_tocadas):
    mais_tocadas = musicas_tocadas[:]
    mais_tocadas.sort(reverse=True)
    menos_tocadas = musicas_tocadas[:]
    menos_tocadas.sort()
    playlist = []
    i = 0
    while len(playlist) != len(musicas_tocadas):
        playlist.append(mais_tocadas[i])
        if menos_tocadas[i] not in playlist:
            playlist.append(menos_tocadas[i])
        i+=1
    return playlist

# def shuffle_musicas(musicas_tocadas):
#     print(musicas_tocadas)
#     mais_tocadas = musicas_tocadas[:]
#     mais_tocadas.sort(reverse=True)
#     menos_tocadas = musicas_tocadas[:]
#     menos_tocadas.sort()
#     playlist = []
#     for i in range(len(musicas_tocadas)):
#         if mais_tocadas[i] not in playlist:
#             playlist.append(mais_tocadas[i])
#         if menos_tocadas[i] not in playlist:
#             playlist.append(menos_tocadas[i])
#         # if len(playlist) >= len(musicas_tocadas):
#         #     break
#     print(playlist)
#     return playlist

print(shuffle_musicas([2,10,5,3]))

