i = 1
num = 1

contador = 0


while num != 0:
    num = int(input(f'Insira o valor do numero {i}, Digite 0 para parar '))
    if num < 200 and num > 100:
        contador = contador + 1
    i = i + 1
print(f'Foram encontrados {contador} numeros entre 100 e 200')    