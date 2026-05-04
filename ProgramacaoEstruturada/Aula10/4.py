valores = []

negativos = 0

for i in range(1, 6):
    valor = int(input(f'Valor {i}: '))
    valores.append(valor)

    if valor < 0:
        negativos += 1

print(negativos) 



