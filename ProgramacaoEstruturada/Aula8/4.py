tempo = float(input("Valor do tempo em minutos "))


horas = int(tempo // 60)

minutos = tempo / 60

intMinutos = int(minutos)

segundos = (intMinutos - minutos) * 60

print(horas, intMinutos, segundos )