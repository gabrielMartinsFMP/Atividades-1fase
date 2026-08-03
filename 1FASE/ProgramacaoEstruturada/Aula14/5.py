inferior = int(input("Escreva o numero inferior: "))
superior = int(input("Escreva o numero superior: "))

numero = inferior + 1

soma = 0

print("Números pares: ")

while numero < superior:
    
    if numero % 2 == 0:
        print(numero)
        soma += numero
    
    numero += 1

print("Soma:", soma)