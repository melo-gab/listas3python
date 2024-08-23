maior=int(input("Insira um valor: "))
menor=maior
for x in range (4):
    num=int(input("Insira um valor: "))
    if num>maior:
        maior=num
    if num<menor:
        menor=num
print("O maior número é", maior, "e o menor número é", menor)