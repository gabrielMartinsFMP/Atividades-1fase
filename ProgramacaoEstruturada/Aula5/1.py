cent1 = int(input("Q° moeda 1 cents: ")) / 100
cent5 = int(input("Q° moeda 5 cents: ")) / 20
cent10 = int(input("Q° moeda 10 cents: ")) /10
cent25 = int(input("Q° moeda 25 cents: ")) /4
cent50 = int(input("Q° moeda 50 cents: ")) /2
cent1r = int(input("Q° moeda 1 real: "))

soma = cent1 + cent5 + cent10 + cent25 + cent50 + cent1r

print(f"A quantidade de reais guardada é: R${soma}")