from math import ceil
def calcula_porcentagem_sorteio(assinante,minutos_assistidos):
    multiplicadores = list(map(lambda assin: 2 if assin else 1 ,assinante))
    viewers = list(zip(multiplicadores,minutos_assistidos))
    horas = list(map(lambda viewer: viewer[0]*ceil(viewer[1]/60), viewers))
    chances = list(map(lambda hora: round(hora/sum(horas)*100),horas))    
    return chances

print(calcula_porcentagem_sorteio([True,False],[60,120]))