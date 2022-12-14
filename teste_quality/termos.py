def calcula_top_ocorrencias_de_queries(texto,queries,k):
    num_ocorrencias = {}
    for termo in queries:
        num_ocorrencias[termo] = texto.count(termo)
    mais_frequentes_ordenado = sorted(num_ocorrencias, key=num_ocorrencias.get, reverse=True)
    return mais_frequentes_ordenado[:k]





print(calcula_top_ocorrencias_de_queries("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",["a","em","i","el"],2))