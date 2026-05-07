valor = int(input('Valor inicial: '))

resultado = 1

for i in range(valor, 0, -1):
    resultado = resultado * i
    print(resultado)
