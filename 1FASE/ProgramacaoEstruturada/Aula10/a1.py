acumulador = 0
contador = 0

for i in range(1, 501):
    if i % 2 == 0:
        acumulador = acumulador + i
        contador = contador + 1

print(f'A quantidade de pares é igual a: {contador}')