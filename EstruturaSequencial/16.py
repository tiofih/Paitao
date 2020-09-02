from math import ceil

mts = float(input("Digite a metragem de parede: "))
qtdLitros = mts / 3
numLatas = ceil(qtdLitros / 18)
preco = numLatas * 80

print("Voce devera comprar", numLatas, "lata e pagara", preco, "reais")
