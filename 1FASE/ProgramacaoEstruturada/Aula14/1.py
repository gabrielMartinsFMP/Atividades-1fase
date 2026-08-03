i = 0
mediaSalario = 0
mediaNumFilho = 0
maiorSalario = 0
salarioAte100 = 0
salario = 0

populacao = 0

while salario >= 0:

    salario = float(input("Escreva seu salario: "))
    
    if salario < 0:
        mediaNumFilhos = mediaNumFilho/populacao
        mediaSalarios = mediaSalario/populacao
        salarioAte100s = salarioAte100/populacao
        break

    populacao = populacao + 1

    filho = float(input("Escreva a quantidade de filhos: "))

    mediaSalario = mediaSalario + salario
    mediaNumFilho = mediaNumFilho + filho

    if maiorSalario < salario:
        maiorSalario = salario
    if salario <= 100:
        salarioAte100 = salarioAte100 + 1

print("A media de salario é", mediaSalarios, " a media de filhos é", mediaNumFilhos, "o maior salario é ", maiorSalario, "percentual de pessoas com 100 reias é ", salarioAte100s)