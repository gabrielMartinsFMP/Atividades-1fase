nome = "a"
media = 0
distancias = []

while nome != "":
    nome = input("Insira o nome do atleta: ")

    if nome == "":
        break

    for i in range(1, 5): 
        distancia = int(input(f"Insira a distancia alcançada numero {i}: "))
        distancias.append(distancia)
    media = sum(distancias) / len(distancias)
    print(f"Nome: {nome} \n Saltos: {distancias} \n Distancia media: {media}")
