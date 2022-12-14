def calcula_total_leds(altura,largura):
    leds = 0
    if altura != 0 and largura != 0:
        leds = (altura+1)*(largura+1)
    return leds

# 1x1 quadrado = 4 vertices
# 2x1 quadrados = 6 vertices
#
# 2x2(4) qudrados = 9 vertices
# 3x2(6) qudrados = 12 vertices
# 4x2(8) qudrados = 15 vertices
# 5x2(10) qudrados = 18 vertices
# 

# cada quadrado tem 1cm de lado
# nos vértices de cada quadrado fica um LED
# na malha 2x4, temos 15 leds, equivalente a (4**2)-1
# 

print(calcula_total_leds(2,3))