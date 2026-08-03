v1 = int(input('V1: '))
v2 = int(input('V2: '))

if v1 > v2:
    maior = v1
    menor = v2
elif v2 > v1:
    maior = v2
    menor = v1
elif v1 == v2:
    print('Os numeros são iguais')

if maior % menor == 0:
    print('Os numeros são multiplos')
else: 
    print('Os numeros não são multiplos')