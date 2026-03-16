# fixo + 4%

price = float(input("valor salario: "))
vendas = float(input("valor vendas: "))

comissao =  vendas * 0.04

print(f"O valor da comissao é igual a R${comissao} e o salario final = R${price + vendas}")