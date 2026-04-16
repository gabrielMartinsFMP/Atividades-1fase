n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))

tipoMedia = input("Digite 'A' para media aritimetica ou 'P' para ponderada")


if tipoMedia == 'A' or tipoMedia == 'a':
    print(f'A media aritimetica é igual a {n1+n2+n3/3}')
elif tipoMedia == 'P' or tipoMedia == 'p':
    print(f'A media ponderada é igual a {((n1*3)+(n2*3)+(n3*4)/3):.1f}')
else: 
    print('insira um valor de media valido')