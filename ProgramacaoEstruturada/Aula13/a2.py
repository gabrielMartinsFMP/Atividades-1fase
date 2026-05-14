nInput = int(input('Insira a quantidade de inputs '))

i = 1


while i <= nInput:
    num = int(input(f'Insira o valor do numero {i} '))
    if num > 0 and num < 25:
        print(f"Num {num} esta no intervalo 0-25")
    elif num > 26 and num < 50:
        print(f"Num {num} esta no intervalo 26-50")
    elif num > 51 and num < 75:
        print(f"Num {num} esta no intervalo 51-75")
    elif num > 76 and num < 100:
        print(f"Num {num} esta no intervalo 76-100")
    
    i = i + 1