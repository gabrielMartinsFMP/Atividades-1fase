n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))




media = (n1 + n2)/2

print(f"Nota = {media:.1f}")
if n1 > 10 or n2 > 10:
    print('Insira notas de acordo com o sistema')
elif media >= 6 :
    print(f'O aluno foi aprovado com nota {media:.1f}')
elif 4 < media < 6:
    print(f'O aluno foi retido com nota {media:.1f}')
else:
    print(f'O aluno foi reprovado com nota {media:.1f}')