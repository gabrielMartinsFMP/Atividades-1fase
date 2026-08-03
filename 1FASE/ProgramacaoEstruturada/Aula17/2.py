lista = [] 
par = 0
impar = 0

for i in range(5):
    valor = int(input("Adicionde o valor do index [i]: "))
    lista.append(valor)

for i in range(len(lista)):
    if lista[i] % 2 ==0:
        par += 1
    else:
        impar += 1

print(f"Pares: {par} \n Impar: {impar}")