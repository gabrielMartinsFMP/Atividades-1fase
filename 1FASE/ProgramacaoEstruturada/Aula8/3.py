n = int(input('Insira um valor entre 1 a 3 '))

while n > 3 or n < 1:
    n = int(input('Insira um valor valido entre 1 a 3! '))

a = int(input('Insira o valor de A '))
b = int(input('Insira o valor de B '))
c = int(input('Insira o valor de C '))

if n == 1:
    if a > b and b > c:
        print(a, b, c)
    elif a > c and c > b:
        print(a, c, b)
    elif b > a and a > c:
        print(b, a, c)
    elif b > c and c > a:
        print(b, c, a)
    elif c > a and a > b:
        print(c, a, b)
    elif c > a and a > b:
        print(c, b, a)
elif n == 2:
    if a > b and b > c:
        print(c, b, a)
    elif a > c and c > b:
        print(b, c, a)
    elif b > a and a > c:
        print(c, a, b)
    elif b > c and c > a:
        print(a, c, b)
    elif c > a and a > b:
        print(b, a, c)
    elif c > a and a > b:
        print(a, b, c)
elif n == 3:
    if a > b and b > c:
        print(c, a, b)
    elif a > c and c > b:
        print(b, a, c)
    elif b > a and a > c:
        print(c, b, a)
    elif b > c and c > a:
        print(a, b, c)
    elif c > a and a > b:
        print(b, c, a)
    elif c > a and a > b:
        print(a, c, b)
    
