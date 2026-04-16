h = float(input('Insira a altura '))

s = input('Insira seu genero (F ou M)')

if s and s == 'F' or s == 'f':
    print(f'Peso ideal: {(72.7*h)-58}')
elif s == 'M' or s == 'm': 
    print(f'Peso ideal: {(62.1*h)-44.7}')
else:
    print('Insira um valor de genero valido')
