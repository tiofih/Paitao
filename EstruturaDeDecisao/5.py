nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if(media < 7):
    print("Voce foi reprovado")
elif (media == 10):
    print("Voce foi aprovado com distincao")
elif(media >= 7):
    print("Voce foi aprovado")
