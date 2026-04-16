h = float(input("altura sua é: "))
p = float(input('peso seu:'))

imc = round(p / (pow(h, 2)), 1)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < imc < 24.9:
    print('peso normal')
elif 25 < imc < 29.9:
    print('sobrepeso')
elif 30 < imc < 35.9:
    print('obesidae 1')
elif 35 < imc < 39.9:
    print('obesidae 2')
else:
    print('Obesidade 3')

