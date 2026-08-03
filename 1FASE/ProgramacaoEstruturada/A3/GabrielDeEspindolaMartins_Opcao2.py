# importa a biblio nativa do python para trabalhar com tempo
import time 

# array com opções do menu a se exibir
menuOptions = ["1 - Mostrar Assentos", "2 - Reservar Assento", "3 - Cancelar Reserva", "4 - Encerrar Sistema"]

# var de opção começando em 1 (poderia ser qualquer numero diferente, pq ela nunca é lida antes do usuario inserir o valor erro de logica)
option = 1

#
i = 1

# variavel jota definida 2x (por erro mas não afeta codigo), se ela não aparecer da erro de variavel não definida
j = 0

# array de fileiras usado para exibir e encontrar valores na matriz
fileira = ["A", "B", "C", "D", "E"]

# array da sala para exibição no menu
sala = [
    ["L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L"], 
    ["L", "L", "L", "L", "L"],  
    ["L", "L", "L", "L", "L"],  
]


# print inicial
print(f"\nBem-vindo ao sistema de Ingresso de Cinema \nInsira uma opção abaixo digitando entre 1-4 \n")

# while true, falso quado num 4 for apertado
while True:

    # pega a função sleep de time que pausa o codigo pra gerar um atraso ao exibir o menu
    time.sleep(0.3)

    # para cada item no array de opções de menu, printeo
    for item in menuOptions:
        print(item)   

    # input de variavel de opção transformado em int
    option = int(input(f" \nInsira uma opção entre 1-4: "))

    # caso num 1 para exibir o array da sala
    if option == 1:

        # variavel jota definida novamente, se ela não aparecer da erro de variavel não definida
        j = 0

        print() #pular linha na exibição
        
        print(" ", end=" ")
        for i in range(1, 6):
            print (i, end=" ")

        print() #pular linha na exibição

        # for para percorrer fileiras (linhas) e exibir de melhor forma, pois somente print(sala), printa todos os colchetes e aspas
        for linha in sala:
            
            # print para exibir as letras das fileiras, end=" " define o caracter final da linha do print, no caso " ", por padrão é \n (pula linha)
            print(fileira[j], end=" ")

            # para cada assento dentro de uma fileira da matriz, printe-a
            for assento in linha:
                print(assento, end=" ")  
            
            # aumenta o valor do contador j para exibição das fileitas
            j = j + 1

            # print para pular linha
            print()
        
        # print para exibir icone de tela
        print("  [T E L A] \n")

    # elif para opção de reservar assento
    elif option == 2:

        #inputs para reservar assento pedindo fileira e numero separadamente
        print("Para reservar o assento insira o valor de sua fileira e numero de assento:")

        # input de fileira com upper para trasnformar em capslock
        f =  input("Fileira: ").upper()
        # while para inserir um valor de fileira valido
        while f not in fileira : 
             f = input("Por favor, insira uma fileira válida: ").upper()

        # input do numero do assento com int
        n = int(input("Numero: "))
        # while para verificar valor correto de 1, 6 (1 a 5)
        while n not in range(1,6): 
            n = int(input("Por favor, insira um numero válido: "))

        # pegando index da coluna da fileira, ele pega o array fileira e usa a função index() 
        # para verificar se um valor existe no array, e pega o valor inteiro do index em sua posição caso exista
        c = int(fileira.index(f))

        #verificando se a poltrona esta livre, acessando a linha e assento da matriz e verificando se esta "L"
        # n-1 é usado pois o python vai começar a contar com 0, mas o usuario e sistema vai trabalhar com 1
        if sala[c][n-1] != "L": 
            print(f"\n Esta poltrona ja está reservada! \n")
        else:
            sala[c][n-1] = "R"
            print(f" \n Poltrona reservada com sucesso! \n")
    
    # elif para opção 3
    elif option == 3:
        
        # variavel booleana de reserva começando em false
        reservas = False
        
        # percorre a matriz procurando por uma reserva "R", se encontrar, da um break e torna o booleano true
        for linha in sala:
            if "R" in linha:
                reservas = True
                break
                
        # caso true, o sistema pergunta qual poltrona deseja cancelar
        if reservas == True:
            print(f"\n Qual poltrona deseja cancelar a reserva? \n")  

            #fileira
            f =  input("Fileira: ").upper()
            # while validando o valor da fileira
            while f not in fileira : 
                f = input("Por favor, insira uma fileira válida: ").upper()

            #n° assento
            n = int(input("Numero: "))
            # while validando numero do assento
            while n not in range(1,6): 
                n = int(input("Por favor, insira um numero válido: "))

            #pegando index da coluna da fileira
            c = int(fileira.index(f))

            # valida se o valor da poltrona é de reservado "R"
            if sala[c][n-1] != "R": 
                print(f"\n Esta poltrona não foi reservada! \n")
            else:
                # se = R, muda o valor da poltrona para L, livre novamente
                sala[c][n-1] = "L"
                print(f" \n Reserva de poltrona cancelada! \n")
        else:
            # se o booleano for falso o sistema só printa que nenhuma reserva foi feita
            print(f" \n Nenhuma reserva foi feita até o momento! \n")     

           
            
    # caso digite op 4, sistema fecha
    if option == 4:
        break