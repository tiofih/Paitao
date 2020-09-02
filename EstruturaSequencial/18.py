from math import ceil

size = float(input("Digite o tamanho do arquivo em MBs: "))
speed = float(input("Digite a velocidade da conexao em Mbps: "))

total = ceil((size / speed) / 60)

print("Voce baixara o arquivo em", total, "minuto")
