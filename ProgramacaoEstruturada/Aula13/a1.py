nInput = int(input('Insira a quantidade de inputs'))

i = 1


while i <= nInput:
    num = int(input(f'Insira o valor do numero {i}'))
    l = num
    acumulador = 1
    while l >= 1:
        acumulador = acumulador * l
        l = l -1
    print(acumulador)
    i = i + 1