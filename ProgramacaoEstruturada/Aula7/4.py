sm = int(input('Valor saldo medio: '))

if sm <= 200 and sm >= 0:
    print('nenhum crédito')
elif sm <= 400 and sm >= 201:
    print('20%')
elif sm <= 600 and sm >= 401:
    print('30%')
elif sm > 601:
    print('40%')