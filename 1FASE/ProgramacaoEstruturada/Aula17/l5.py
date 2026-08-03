cartas = []

for i in range(2,10):
    cartas.append(i)

for i in range(len(cartas)):
    for j in range(1, 4):
        cartas.append(cartas[i])

cartas.sort()
print(cartas)