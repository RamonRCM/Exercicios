def retorna_menor_e_maior_valor_de_vendas(tickets):
    vendas = []
    for funcionario in tickets:
        for venda in funcionario:
            if 20 <= venda <= 500:
                vendas.append(venda)
    retorno = [min(vendas),max(vendas)]
    return retorno

print(retorna_menor_e_maior_valor_de_vendas([[200,100],[300],[],[10,900]]))

# [2, 20, 300, 700]
# [2, 40, 500, 700]