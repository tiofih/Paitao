num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
prim = 0
seg = 0
terc = 0

if(num1 > num2 and num1 > num3):
    prim = num1
    if(num2 > num3):
        terc = num2
        seg = num3
    elif (num2 < num3):
        terc = num3
        seg = num2
    else:
        terc = num3
        seg = num2
elif (num2 > num1 and num2 > num3):
    prim = num2
    if(num1 > num3):
        seg = num1
        terc = num3
    elif(num1 < num3):
        seg = num3
        terc = num1
    else:
        seg = num3
        terc = num1
elif (num3 > num1 and num3 > num2):
    prim = num3
    if(num1 > num2):
        seg = num1
        terc = num2
    elif(num1 < num2):
        seg = num2
        terc = num1
    else:
        seg = num2
        terc = num1
else:
    prim = num1
    seg = num2
    terc = num3

print(prim, seg, terc)
