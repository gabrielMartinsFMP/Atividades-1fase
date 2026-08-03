nInput = int(input('Insira a quantidade de inputs'))

i = 1
soma = 0

while i <= nInput:
    num = int(input(f'Insira o valor do numero {i}'))

    soma = soma + num
   
    i = i + 1

print(soma)