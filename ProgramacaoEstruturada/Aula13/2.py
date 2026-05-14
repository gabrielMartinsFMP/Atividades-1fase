inicio = int(input('valor inicio '))
final = int(input('valor final '))

soma3 = 0

i = inicio
while i <= final:
    if i % 3 == 0:
        soma3 = soma3 + i
    i = i + 1

print(soma3)
