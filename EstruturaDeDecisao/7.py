num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if(num1 > num2 and num1 > num3):
    print("O primeiro numero e maior")
    if(num2 > num3):
        print("E o terceiro numero e menor")
    else:
        print("E o segundo numero e menor")
elif(num2 > num1 and num2 > num3):
    print("O segundo numero e maior")
    if(num1 > num3):
        print("E o terceiro numero e menor")
    else:
        print("E o primeiro numero e menor")
elif(num3 > num1 and num3 > num2):
    print("O terceiro numero e maior")
    if(num1 > num2):
        print("E o segundo numero e menor")
    else:
        print("E o primeiro numero e menor")
else:
    print("Alguns numeros sao iguais")
