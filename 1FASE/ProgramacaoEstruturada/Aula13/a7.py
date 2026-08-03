i = 1
num = 1
mNum = 0
contador = 0


while num != -1:
    num = int(input(f'Insira o valor do numero {i}, Digite -1 para parar '))
    if num > mNum:
        mNum = num
    i = i + 1
print(f'o maior numero foi {mNum}')    