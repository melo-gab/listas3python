num=int(input("Insira um número: "))
exp=int(input("Insira um expoente: "))
resultado=1
for x in range (exp):
    resultado*=num
print(num, "elevado a", exp, "é igual a", resultado)