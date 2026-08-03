alturas = []
altura = 1
maiorAltura = 0
menorAltura = 0

while altura != 0:
    altura = int(input("Qual a sua altura?: "))
    alturas.append(altura)

    if altura > maiorAltura:
        maiorAltura = altura

    elif altura > menorAltura:
        menorAltura = altura

print(alturas)
print("maiorAltura: ", maiorAltura)
print("menorAltura: ", menorAltura)
