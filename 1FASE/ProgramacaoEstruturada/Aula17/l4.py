import random

# Initialize a dictionary to store counts for faces 1 to 6
contador = {i: 0 for i in range(1, 7)}
jogadas = []

# Roll the die 100 times
for i in range(100):
    num = random.randint(1, 6)
    jogadas.append(num)
    contador[num] += 1  # Increment the count for the rolled number

# Print the history of all rolls
print("Jogadas:", jogadas)
print("\nContagem de cada número:")

# Print the results for each face
for i in range(1, 7):
    print(f"Número {i}: {contador[i]} vezes")
