def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    tf1,vqr1,tf2,vqr2 = float(tf1),float(vqr1),float(tf2),float(vqr2)

    if tf1 == tf2 and vqr1 == vqr1:
        return "Tanto faz"
    elif tf1 >= tf2 and vqr1 >= vqr2:
        return "Empresa 2"
    elif tf1 <= tf2 and vqr1 < vqr2:
        return "Empresa 1"
    elif vqr1  < vqr2:
        perto = 2
        longe = 1
    else:
        perto = 1
        longe = 2

    distancia = round((tf1 - tf2)/(vqr2-vqr1),2)
    return (
        f"Empresa {perto} quando a distância < {distancia}, Tanto faz quando a distância = {distancia}, Empresa {longe} quando a distância > {distancia}")

    

        
    

    return texto

print(escolhe_taxi("2.5","1.0","5.0","0.75"))