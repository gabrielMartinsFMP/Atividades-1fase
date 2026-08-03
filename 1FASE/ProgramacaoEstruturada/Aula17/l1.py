celsius = [0, 15, 40]
farenheit = []
for i in range(len(celsius)):
    farenheit.append((celsius[i] * 1.8) + 32)

print(farenheit)