def calcula_numero_da_senha(senha):
    colunas = []
    final_senha = ''
    string_coluna = ''
    for i in range(0,10):
        for linha in senha:
            string_coluna += linha[i]
        colunas.append(string_coluna)
        string_coluna = ''
    for texto in colunas:
        if texto.count('1') >=5:
            final_senha+='1'
        else:
            final_senha+='0'
    return int(final_senha,2)


print(calcula_numero_da_senha([
    "0110100000",
    "1001011111",
    "1110001010",
    "0111010101",
    "0011100110",
    "1010011001",
    "1101100100",
    "1011010100",
    "1001100111",
    "1000011000"]
    #1011010100
))