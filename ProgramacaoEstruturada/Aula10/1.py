alturas = []
maiorAltura = 0
menorAltura = 0

for i in range(15):
    valor = float(input(f'Altura: '))
    alturas.append(valor)

    if valor > maiorAltura:
        maiorAltura = valor
    elif valor < menorAltura:
        menorAltura = valor

print(f'\n A menor altura é {menorAltura}')
print(f'\n A maior altura é {maiorAltura}')