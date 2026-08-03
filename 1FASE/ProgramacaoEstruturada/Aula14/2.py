nume = 1
deno = 2

soma = 0

while nume <= 99 and deno <= 50:
    if (nume/deno) % 2 == 0 and (nume/deno) % 3 == 0:
        soma = (nume/deno) + soma
    nume = nume + 2
    deno = deno + 1


print(soma)
