n = int(input('num: '))

if n % 2 == 0:
    print('o num é par')
else:
    print('num impar')

if n > 0:
    print('num positivo')
elif n == 0:
    print('num neutro')
else: 
    print('num negativo')