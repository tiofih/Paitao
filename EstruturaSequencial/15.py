sal = float(input("Digite o valor que tu ganha por hora: "))
hrs = float(input("Digite quantas horas tu trabalhou neste mes: "))
salBruto = sal * hrs
impRenda = salBruto * 0.11
inss = salBruto * 0.08
sind = salBruto * 0.05
salLiq = salBruto - (impRenda + inss + sind)

print("+ Salário Bruto : R$ " + str(salBruto))
print("+- IR (11 % ): R$ " + str(impRenda))
print("+- INSS (8 % ): R$ " + str(inss))
print("+- Sindicato (5 %): R$ " + str(sind))
print("+= Salário Liquido: R$ " + str(salLiq))
