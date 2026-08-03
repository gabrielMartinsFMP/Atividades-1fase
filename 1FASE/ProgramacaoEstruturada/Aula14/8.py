num = int(input("Insira o valor inteiro e positivo"))
soma = 0
while num <= 0:
    num = int(input("Insira um valor valido!"))


for i in range(1, num + 1):
    soma = (1/i) + soma
    print(soma)