def ultima_parada(combustivel,consumo,postos_de_gasolina):
    distancia = consumo*combustivel
    postos_de_gasolina.sort(reverse=True)
    parada = -1
    for posto in postos_de_gasolina:
        if posto <= distancia:
            parada = posto
            break
    return parada
    
    
        

print(ultima_parada(2,8,[2,15,22,11]))