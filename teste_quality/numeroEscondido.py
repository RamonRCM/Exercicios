import re
def checa_numero_escondido(numero,numero_oculto):
    regex = r".*"
    resposta = False
    for character in str(numero_oculto):
        regex+=f"{character}.*"
    if re.search(regex,str(numero)):
        resposta = True
    return resposta
print(checa_numero_escondido(12345,235))