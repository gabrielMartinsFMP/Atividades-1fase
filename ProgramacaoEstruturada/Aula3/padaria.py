qBroa = int(input("Qual foi a quantidade de broas? "))
qFrances = int(input("Qual foi a quantidade de pão franceses? "))

valorB = 1.5 * qBroa
valorF = 0.12 * qFrances

total = valorB + valorF

poupanca = total * 0.1

print(f"O valor total arrecadado no dia foi {total}, a partir da soma de {valorB} com {valorF}. 10% deve ser guardado na poupança que é igual a {poupanca}.")