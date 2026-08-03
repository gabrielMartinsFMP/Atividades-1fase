
lista = []
tamanhoLista = int(input("Insira o tamanho da lista de nums: "))

for i in range(tamanhoLista):
    num = int(input(f"Insira o valor {i+1}: "))
    lista.append(num)
    
print(lista)