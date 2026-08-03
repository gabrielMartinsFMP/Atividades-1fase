maiorH = 0
menorH = float('inf') 
totalH = 0
totalHfem = 0
contadorFem = 0

total_pessoas = 3

for i in range(total_pessoas):
    altura = float(input(f"Pessoa {i+1} - Qual sua Altura: ? "))
    sexo = int(input(f"Pessoa {i+1} - Qual seu sexo? (1 para feminino e 0 para masculino): "))
    
    while sexo != 0 and sexo != 1:
        sexo = int(input("Insira um valor valido! (0 ou 1): "))

    if altura > maiorH:
        maiorH = altura
    if altura < menorH:
        menorH = altura

    if sexo == 0:
        totalH = totalH + 1
    elif sexo == 1:
        totalHfem = totalHfem + altura
        contadorFem = contadorFem + 1
  
if contadorFem > 0:
    mediaF = totalHfem / contadorFem
else:
    mediaF = 0

mediaT = totalH / total_pessoas

print("-" * 30)
print(f"A maior altura é: {maiorH}")
print(f"A menor altura é: {menorH}")
print(f"A média de altura feminina é: {mediaF:.2f}")