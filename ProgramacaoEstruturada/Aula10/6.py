nome = input("insira seu nome completo")

tamanhoNome = 0

for i in nome:
    if i != ' ':
        tamanhoNome = tamanhoNome +1
    elif i == ' ':
        break

print(f'tamanho: {tamanhoNome}')