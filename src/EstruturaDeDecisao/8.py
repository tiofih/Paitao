prod1 = int(input("Digite o primeiro preco: "))
prod2 = int(input("Digite o segundo preco: "))
prod3 = int(input("Digite o terceiro preco: "))

if(prod1 < prod2 and prod1 < prod3):
    print("Voce deve comprar o primeiro produto")
elif(prod2 < prod1 and prod2 < prod3):
    print("Voce deve comprar o segundo produto")
elif(prod3 < prod1 and prod3 < prod2):
    print("Voce deve comprar o terceiro produto")
