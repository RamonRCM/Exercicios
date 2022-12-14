from math import ceil
def calcula_porcentagem_sorteio(assinante,minutos_assistidos):
    lista_horas = []
    chances = []
    for i in range(len(minutos_assistidos)):
        if assinante[i] == True:
            lista_horas.append(ceil(minutos_assistidos[i]/60)*2)
        else:
            lista_horas.append(ceil(minutos_assistidos[i]/60))
    for elemento in lista_horas:
        chances.append(round(elemento*100/sum(lista_horas)))
    return chances

print(calcula_porcentagem_sorteio([True,False],[60,120]))