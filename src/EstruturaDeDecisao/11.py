sal = float(input("Digite o salario que tu recebe atualmente: "))

percent: float
aumento: float
salTotal: float

if(sal <= 280):
    percent = 0.2
elif(sal > 280 and sal <= 700):
    percent = 0.15
elif(sal > 700 and sal <= 1500):
    percent = 0.1
elif (sal > 1500):
    percent = 0.05

aumento = sal * percent
salTotal = sal + aumento

print("Seu salario era de ", sal, "reais")
print("Voce teve um aumento de", (percent * 100), "%")
print("Gerando", aumento, "reais a mais")
print("Sendo seu salario agora de", salTotal, "reais")
