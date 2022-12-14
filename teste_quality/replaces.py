def menor_string_maior(name):
  texto = ""

  for i in range(len(name)-1, 0, -1):
    if name[i] > name [i-1]:
        inicio_palavra = name[0:(i-1)] + name[i]
        final_palavra = ''.join(sorted(name[i-1] + name[(i+1):]))
        texto = inicio_palavra + final_palavra
        return texto
  return "sem resposta"

print(menor_string_maior("abcde"))