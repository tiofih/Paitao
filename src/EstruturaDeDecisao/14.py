x = float(input("Digite a primeira nota: "))
y = float(input("Digite a segunda nota: "))

media = (x + y) / 2

if(media <= 4):
    print("Voce tirou um E")
    print("Sua media foi de", media)
    print("E voce esta Reprovado")
elif(media <= 6):
    print("Voce tirou um D")
    print("Sua media foi de", media)
    print("E voce esta Reprovado")
elif(media <= 7.5):
    print("Voce tirou um C")
    print("Sua media foi de", media)
    print("E voce esta Aprovado")
elif(media <= 9):
    print("Voce tirou um B")
    print("Sua media foi de", media)
    print("E voce esta Aprovado")
elif(media <= 10):
    print("Voce tirou um A")
    print("Sua media foi de", media)
    print("E voce esta Aprovado")
