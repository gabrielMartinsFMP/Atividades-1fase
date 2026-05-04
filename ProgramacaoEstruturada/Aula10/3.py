valorInicial = int(input('Valor inicial: '))


fatorial = 1

for i in range(1, valorInicial + 1):
    fatorial = fatorial * i

print(fatorial)