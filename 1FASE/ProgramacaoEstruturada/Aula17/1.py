lista = []

qIndex = int(input("Insira a quantidade de indices:"))

for i in range(qIndex): 
    valor = int(input(f'insira valor {i}: '))
    lista.insert(0, valor)
    #pode usar .reverse() no final para reverter o array

print(lista)