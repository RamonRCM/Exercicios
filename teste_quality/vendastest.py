def retorna_menor_e_maior_valor_de_vendas(tickets):
    maiores_vendedor = []
    menores_vendedor = []
    for vendedor in tickets:
        if not vendedor:
            continue
        maiores_vendedor.append(max(vendedor))
        menores_vendedor.append(min(vendedor))
    
    
    maior_menor_venda = [min(menores_vendedor),max(maiores_vendedor)]
    return maior_menor_venda

print(retorna_menor_e_maior_valor_de_vendas([[200,100],[300],[],[20,900]]))
# [2, 20, 300, 700]
# [2, 40, 500, 700]