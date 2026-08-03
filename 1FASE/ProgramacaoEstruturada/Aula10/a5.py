tabuada = int(input('Informe a tabuada desejada: '))
inicial = int(input('Qual valor inicia? '))
final = int(input('Qual valor finaliza? '))

for i in range (inicial, final+1):
    print(f'{tabuada} x {i} = {tabuada * i}')
    i = i + 1