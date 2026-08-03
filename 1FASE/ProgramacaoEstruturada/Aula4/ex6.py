hT = int(input("Valor horas trabalhadas: ")) * 10.00
hE = int(input("Valor horas extras: ")) * 15.00

sBruto = hT + hE
sLiquido = sBruto - (sBruto * 0.1)

print(f"o salario bruto é igual a R${sBruto} e liquido R${sLiquido}")