i = 1
acumulador = 0
while i <= 10:
    num = int(input(f'Insira o valor do numero {i} '))
    if num < 0:
        acumulador = acumulador + num
    i = i + 1
print(acumulador)    
