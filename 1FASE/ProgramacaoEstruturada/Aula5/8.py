anoNasc = int(input("Ano nasc: "))
anoAtual = int(input("ano atual: "))

oldAnos = anoAtual - anoNasc
oldMeses = oldAnos * 12
oldDias = oldAnos * 365
oldSemanas = 48

print(f"Q° anos vividos: {oldAnos} \n Q° meses vividos: {oldMeses} \n Q° dias vividos: {oldDias} \n Q° semanas vividos: {oldSemanas}")