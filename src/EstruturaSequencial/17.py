from math import ceil

mts = float(input("Digite a metragem de parede: "))
qtdLitros = mts / 6

numLatasMaior = ceil(qtdLitros / 18)
numLatasMenor = ceil(qtdLitros / 3.6)

restoMaior = ceil(float("{0:.1f}".format(qtdLitros % 3.6)) / 18)
restoMenor = ceil((mts - (restoMaior * 108)) / (6 * 3.6))

precoMaior = numLatasMaior * 80
precoMenor = numLatasMenor * 25
precoTotal = (restoMaior * 80) + (restoMenor * 25)

print(restoMaior)
print("Voce devera comprar", numLatasMaior,
      "latas de 18 litros e pagara", precoMaior, "reais")
print("Ou comprar", numLatasMenor,
      "latas de 3,6 litros e pagara", precoMenor, "reais")
print("Ou comprar comprar", restoMaior,
      "latas de 18 litros e", restoMenor, "latas de 3,6 litros e pagara", precoTotal, "reais")
