n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))
me = int(input('Qual a media dos exercicios? '))

ma = (n1 + (n2*2) + (n3*3) + me)/7
ma = round(ma, 2)


if ma >= 9:
    print(f'Aprovado com conceito A e nota de aproveitamento {ma}')
elif ma >= 7.5 and ma < 9:
    print(f'Aprovado com conceito B e nota de aproveitamento {ma}')
elif ma >= 6 and ma < 7.5:
    print(f'Aprovado com conceito C e nota de aproveitamento {ma}')
elif ma >= 4 and ma < 6:
    print(f'Reprovado com conceito D e nota de aproveitamento {ma}')
elif ma < 4:
    print(f'Reprovado com conceito E e nota de aproveitamento {ma}')