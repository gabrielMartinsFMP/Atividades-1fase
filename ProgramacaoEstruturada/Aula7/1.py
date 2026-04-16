idade = int(input('idade: '))

if 0 < idade <= 4:
    print('n atendemos essa idade')
elif 5 < idade <= 7:
    print('infantil A')
elif 8 < idade <= 10:
    print('infantil B')
elif 11 < idade <= 13:
    print('Juvenil A')
elif 14 < idade <= 17:
    print('Juvenil B')
elif idade >= 18:
    print('Adulto')