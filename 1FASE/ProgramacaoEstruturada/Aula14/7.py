idade = 0
somaMaior = 0
mediaMaior = 0
total = 0

while idade >= 0:
    
    idade = int(input("Escreva a idade: "))
    if idade < 0:
        break
    total += 1
    if idade >= 18:
        somaMaior += idade
        mediaMaior += 1
    
mediaMaiors = mediaMaior/total

print("Soma das pessoas maior de idade:", somaMaior, "e a média maior de idade: ", mediaMaiors)