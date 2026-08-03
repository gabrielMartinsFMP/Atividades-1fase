import time

menuOptions = ["1 - Mostrar Assentos", "2 - Reservar Assento", "3 - Cancelar Reserva", "4 - Encerrar Sistema"]

option = 0

i = 1
j = 0

fileira = ["A", "B", "C", "D", "E"]

sala = [
    ["L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L"], 
    ["L", "L", "L", "L", "L"],  
    ["L", "L", "L", "L", "L"],  
]

print(f"\nBem-vindo ao sistema de Ingresso de Cinema \nInsira uma opção abaixo digitando entre 1-4 \n")

while True:
    time.sleep(0.3)
    
    for item in menuOptions:
        print(item)   

    option = int(input(f" \nInsira uma opção entre 1-4: "))

    if option == 1:
        j = 0

        print() #pular linha na exibição
        
        print(" ", end=" ")
        for i in range(1, 6):
            print (i, end=" ")

        print() #pular linha na exibição

        for linha in sala:

            print(fileira[j], end=" ")

            for assento in linha:
                print(assento, end=" ")  
            
            j = j + 1
            print()
            
        print("  [T E L A] \n")


    elif option == 2:

        #inputs para reservar assento
        print("Para reservar o assento insira o valor de sua fileira e numero de assento:")

        f =  input("Fileira: ").upper()
        while f not in fileira : 
             f = input("Por favor, insira uma fileira válida: ").upper()

        n = int(input("Numero: "))
        while n not in range(1,6): 
            n = int(input("Por favor, insira um numero válido: "))

        #pegando index da coluna da fileira
        c = int(fileira.index(f))

        #verificando se a poltrona esta livre
        if sala[c][n-1] != "L": 
            print(f"\n Esta poltrona ja está reservada! \n")
        else:
            sala[c][n-1] = "R"
            print(f" \n Poltrona reservada com sucesso! \n")
        
    elif option == 3:
        reservas = False

        for linha in sala:
            if "R" in linha:
                reservas = True
                break
                
        if reservas == True:
            print(f"\n Qual poltrona deseja cancelar a reserva? \n")  
            f =  input("Fileira: ").upper()
            while f not in fileira : 
                f = input("Por favor, insira uma fileira válida: ").upper()

            n = int(input("Numero: "))
            while n not in range(1,6): 
                n = int(input("Por favor, insira um numero válido: "))

            #pegando index da coluna da fileira
            c = int(fileira.index(f))

            if sala[c][n-1] != "R": 
                print(f"\n Esta poltrona não foi reservada! \n")
            else:
                sala[c][n-1] = "L"
                print(f" \n Reserva de poltrona cancelada! \n")
        else:
            print(f" \n Nenhuma reserva foi feita até o momento! \n")     

           
            

    if option == 4:
        break