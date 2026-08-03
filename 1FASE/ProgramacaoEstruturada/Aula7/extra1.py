h1 = int(input('idade homem 1'))
h2 = int(input('idade homem 2'))

m1 = int(input('idade mulher 1'))
m2 = int(input('idade mulher 2'))

if h1 >= h2:
    maiorH = h1
    menorH = h2
elif h2 >= h1:
    maiorH = h2
    menorH = h1

if m1 >= m2:
    maiorM = m1
    menorM = m2
elif m2 >= m1:
    maiorM = m2
    menorM = m1

soma = maiorM + menorM

produto = menorH + maiorM

print(f'soma das idades do homem mais velho com a mulher mais nova {soma} \n o produto das idades do homem mais novo com a mulher mais velha {produto}')