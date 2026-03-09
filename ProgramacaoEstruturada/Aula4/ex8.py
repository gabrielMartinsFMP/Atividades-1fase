import math

conta = float(input('Valor total da conta: R$ '))

carlos = math.floor(conta / 3)
andre = math.floor(conta / 3)
felipe = conta - carlos - andre

print(f'Carlos paga: R$ {carlos:.2f}')
print(f'André paga: R$ {andre:.2f}')
print(f'Felipe paga: R$ {felipe:.2f}')
