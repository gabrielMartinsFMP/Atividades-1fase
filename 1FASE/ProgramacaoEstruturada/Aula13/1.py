

soma = 0
par = 0
impar = 0
i = 0
while i <= 10:
    soma = soma + i
    if i % 2 == 0:
        par = par + i
    elif i % 2 != 0:
        impar = impar + i
    i = i + 1

print(soma)
print(impar)
print(par)