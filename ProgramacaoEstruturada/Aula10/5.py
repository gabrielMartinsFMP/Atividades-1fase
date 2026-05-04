
c1 = 0
c2 = 0
c3 = 0
c4 = 0
vn = 0
vb = 0

for i in range(100):
    valor = int(input('tipo de voto, 1-6:'))
    if valor == 1:
        c1 = c1 + 1
    elif valor == 2:
        c2 = c2 + 1
    elif valor == 3:
        c3 = c3 + 1
    elif valor == 4:
        c4 = c4 + 1
    elif valor == 5:
        vn = vn + 1
    elif valor == 6:
        vb = vb + 1

print(f"total canditato 1: {c1} \n total canditato 2: {c2} \n total canditato 3: {c3} \n total canditato 4: {c4} \n total nulos: {vn} \n total brancos {vb}")
    