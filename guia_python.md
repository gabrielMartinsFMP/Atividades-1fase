Python
Guia de Introducao a Logica de Programacao
Para quem esta comecando do zero


O que voce vai aprender neste guia
Unidade I   — Variaveis, Entrada e Saida de Dados
Unidade II  — Operadores Aritmeticos, Relacionais e Logicos
Unidade III — Estrutura de Decisao (if, elif, else)
Unidade IV  — Lacos de Repeticao (for, while)
Unidade V   — Listas e Matrizes
Unidade VI  — Funcoes


Como usar este guia
Cada unidade comeca com uma explicacao simples do conceito, como se estivessemos conversando. Depois, exemplos de codigo progressivos mostram como aplicar o que foi explicado. Caixas coloridas destacam dicas importantes, erros comuns e conceitos-chave. Ao final de cada unidade, um resumo rapido ajuda a fixar os principais pontos.
Leia com calma, teste os codigos no seu computador e nao pule as caixas coloridas — elas foram feitas para salvar voce dos erros mais comuns!

Nao precisa memorizar tudo de uma vez!
Programacao se aprende fazendo. Use este guia como referencia enquanto resolve os exercicios. Com o tempo, os conceitos se tornam naturais.
UNIDADE I
Variaveis, Entrada e Saida de Dados
Como o Python guarda e exibe informacoes


O que e uma variavel?
Imagine que voce tem uma caixa com um nome escrito nela. Voce coloca alguma coisa dentro dessa caixa e, sempre que quiser, pode pegar o que esta la dentro so chamando pelo nome. Isso e exatamente o que e uma variavel em programacao: um espaco na memoria do computador com um nome, que guarda um valor.
Em Python, criar uma variavel e simples: voce escolhe um nome, usa o sinal de igual (=) e escreve o valor. Nao precisa declarar o tipo antes, como em outras linguagens. O Python descobre o tipo automaticamente.
Como criar uma variavel
# Criando variaveis
nome = "Ana"
idade = 20
altura = 1.65
esta_matriculada = True




Conceito: O sinal = em Python
O sinal = nao significa 'igual' como na matematica.
Ele significa 'recebe' ou 'armazena'. Leia nome = 'Ana' como: a variavel nome recebe o valor Ana.


Tipos de Dados
Cada valor que você armazena em uma variavel tem um tipo. Conhecer os tipos e importante porque determina o que voce pode fazer com aquele valor (somar numeros, concatenar textos, etc).

Tipo
O que guarda
Exemplo
str
Textos e palavras
"Ola, mundo!"
int
Numeros inteiros
10, -5, 0, 200
float
Numeros com virgula (decimais)
3.14, 1.75, -0.5
bool
Verdadeiro ou Falso
True, False


nome     = "Carlos"      # str  — texto entre aspas
pontos   = 85             # int  — numero inteiro
media    = 8.5            # float — numero decimal
aprovado = True           # bool — verdadeiro/falso

# Verificando o tipo de uma variavel
print(type(nome))         # <class 'str'>
print(type(pontos))       # <class 'int'>




Dica: Nomes de variaveis
Use nomes descritivos: idade_aluno e melhor que x.
Use letras minusculas e underscore para separar palavras: nome_completo.
Nao comece com numero: 2nome e invalido.
Python diferencia maiusculas de minusculas: Nome e nome sao variaveis diferentes.


Conversao de Tipos (casting)
Muitas vezes voce vai precisar converter um tipo em outro. Por exemplo, o input() sempre retorna texto (str), mas se voce quer fazer calculos, precisa converter para int ou float.
# Convertendo tipos
numero_texto = "42"
numero_inteiro = int(numero_texto)      # str -> int
numero_decimal = float(numero_texto)    # str -> float
texto_numero = str(numero_inteiro)      # int -> str

print(numero_inteiro + 8)   # 50  (funciona como numero)
print(numero_texto + "8")   # 428 (junta textos!)




Atencao!: Erro comum de iniciante
Tentar somar um numero digitado pelo usuario sem converter:
  idade = input('Digite sua idade: ')  # retorna texto!
  ano_nascimento = 2025 - idade        # ERRO: nao da para subtrair texto de numero
A solucao e converter: idade = int(input('Digite sua idade: '))


Entrada de Dados com input()
A funcao input() pausa o programa e aguarda o usuario digitar algo. O que o usuario digitar sera armazenado em uma variavel. Sempre exiba uma mensagem dentro do input() para orientar o usuario.
# Sintaxe basica do input()
variavel = input("Mensagem para o usuario: ")

# Exemplos praticos
nome = input("Qual e o seu nome? ")
idade = int(input("Qual e a sua idade? "))
altura = float(input("Qual e a sua altura (em metros)? "))




Lembre-se: input() sempre retorna str
Independente do que o usuario digitar, o input() sempre devolve uma string.
Se voce quiser um numero, SEMPRE converta com int() ou float().
Exemplo completo: nota = float(input('Digite a nota: '))


Saida de Dados com print()
A funcao print() exibe informacoes na tela. E a principal forma de mostrar resultados para o usuario. Voce pode exibir textos, variaveis, calculos e muito mais.
nome = "Ana"
idade = 22

# Formas de usar o print()
print("Ola, mundo!")                   # texto simples
print(nome)                             # valor de variavel
print("Nome:", nome, "- Idade:", idade) # varios valores separados por virgula
print("Resultado:", 2 + 3)              # calculo direto

f-strings: a forma moderna e elegante
As f-strings sao a maneira mais pratica de misturar texto e variaveis em Python. Coloque um f antes das aspas e use chaves {} para inserir variaveis ou expressoes.
nome = "Carlos"
idade = 20
media = 8.75

# f-string: coloque f antes das aspas
print(f"Ola, {nome}!")
print(f"Voce tem {idade} anos.")
print(f"Sua media e: {media}")
print(f"Media formatada: {media:.2f}")  # 2 casas decimais -> 8.75

# Resultado:
# Ola, Carlos!
# Voce tem 20 anos.
# Sua media e: 8.75


Recurso no print()
O que faz
Exemplo
sep=
Muda o separador entre itens
print("a","b", sep="-")  ->  a-b
end=
Muda o que aparece no final
print("Ola", end=" ")  -> sem quebra de linha
{:.2f}
Formata float com 2 casas
f"{3.14159:.2f}"  ->  3.14
{:>10}
Alinha o texto a direita em 10 espacos
f"{nome:>10}"


Comentarios no codigo
Comentarios sao linhas que o Python ignora completamente. Eles existem para voce (e outros programadores) entenderem o que o codigo faz. Use sempre que uma parte do codigo nao for obvio.
# Isto e um comentario de linha — o Python ignora tudo depois do #
nome = "Ana"  # comentario pode aparecer apos o codigo

# Boas praticas:
# - Comente o PORQUE, nao o O QUE (o codigo ja mostra o que faz)
# - Mantenha comentarios curtos e diretos
# - Atualize comentarios quando mudar o codigo


Resumo da Unidade I
variavel = valor   — cria ou atualiza uma variavel
input("mensagem")   — le entrada do usuario (sempre str)
print(valor)   — exibe na tela
int()  float()  str()   — convertem tipos
f"texto {variavel}"   — f-string para formatar saida


UNIDADE II
Operadores Aritmeticos, Relacionais e Logicos
As ferramentas de calculo e comparacao do Python


Os operadores sao os simbolos que permitem ao Python realizar calculos, comparar valores e tomar decisoes logicas. Eles sao a base de toda a logica de programacao.
Operadores Aritmeticos
Sao os operadores matematicos classicos. Eles trabalham com numeros (int e float) e retornam um resultado numerico.
Operador
Operacao
Exemplo
Resultado
+
Adicao
10 + 3
13
-
Subtracao
10 - 3
7
*
Multiplicacao
10 * 3
30
/
Divisao (real)
10 / 3
3.333...
//
Divisao inteira
10 // 3
3
%
Modulo (resto)
10 % 3
1
**
Potenciacao
2 ** 8
256


a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333333333333335  (sempre retorna float)
print(a // b)   # 3   (descarta a parte decimal)
print(a % b)    # 1   (resto da divisao: 10 = 3*3 + 1)
print(2 ** 8)   # 256 (2 elevado a 8)




Dica: Quando usar // e %?
// e util para saber quantas vezes um numero cabe em outro. Ex: 17 // 5 = 3 (cabe 3 vezes).
% e util para saber se um numero e par ou impar: se numero % 2 == 0, e par.
Tambem e util para verificar multiplos: se numero % 3 == 0, e multiplo de 3.


Precedencia de operadores (ordem de execucao)
Python segue a mesma ordem da matematica: primeiro potencias, depois multiplicacao/divisao, depois adicao/subtracao. Use parenteses para forcar a ordem que voce quer.
# Sem parenteses — segue a ordem matematica
resultado = 2 + 3 * 4      # 14 (primeiro 3*4=12, depois 2+12)

# Com parenteses — voce controla a ordem
resultado = (2 + 3) * 4    # 20 (primeiro 2+3=5, depois 5*4)

# Calculo de IMC como exemplo
peso = 70.0
altura = 1.75
imc = peso / (altura ** 2)  # parenteses sao necessarios aqui!
print(f"IMC: {imc:.2f}")    # IMC: 22.86


Atalhos de atribuicao (operadores compostos)
Python tem atalhos que combinam uma operacao aritmetica com a atribuicao. Sao muito usados em contadores e acumuladores.
contador = 0
contador += 1    # equivale a: contador = contador + 1  -> 1
contador += 1    # -> 2
contador -= 1    # equivale a: contador = contador - 1  -> 1
contador *= 3    # equivale a: contador = contador * 3  -> 3
contador //= 2   # equivale a: contador = contador // 2 -> 1


Operadores Relacionais
Os operadores relacionais comparam dois valores e retornam um resultado booleano: True (verdadeiro) ou False (falso). Sao fundamentais para as estruturas de decisao (if/else).
Operador
Significado
Exemplo
Resultado
==
Igual a
5 == 5
True
!=
Diferente de
5 != 3
True
>
Maior que
7 > 3
True
<
Menor que
2 < 1
False
>=
Maior ou igual a
5 >= 5
True
<=
Menor ou igual a
4 <= 3
False


nota = 7.5

print(nota >= 7.0)   # True  — nota e maior ou igual a 7.0?
print(nota == 10)    # False — nota e exatamente 10?
print(nota != 5)     # True  — nota e diferente de 5?

# Comparando strings
nome = "Ana"
print(nome == "Ana")   # True  (comparacao exata, com maiusculas)
print(nome == "ana")   # False (diferente! Python e case-sensitive)




Atencao!: = (atribuicao) vs == (comparacao)
= e para guardar um valor em uma variavel: idade = 20
== e para comparar dois valores: if idade == 18:
Este e um dos erros mais comuns: usar = quando queria ==.


Operadores Logicos
Os operadores logicos combinam duas ou mais comparacoes em uma unica expressao. Permitem verificar condicoes mais complexas, como: 'a nota e maior que 5 E o aluno nao esta reprovado'.
Operador
Funciona assim
Exemplo
Resultado
and
Verdadeiro se AMBOS forem True
5 > 3 and 10 > 7
True
or
Verdadeiro se PELO MENOS UM for True
5 > 10 or 3 > 1
True
not
Inverte o resultado
not True
False


nota = 6.5
frequencia = 80

# and: as DUAS condicoes precisam ser verdadeiras
aprovado = nota >= 7 and frequencia >= 75
print(aprovado)   # False (nota < 7, entao falha no primeiro)

# or: PELO MENOS UMA condicao precisa ser verdadeira
pode_tentar = nota >= 5 or frequencia >= 90
print(pode_tentar)   # True (nota >= 5 e verdadeiro)

# not: inverte
reprovado = not aprovado
print(reprovado)   # True




Dica: Dica para lembrar os operadores logicos
and = 'E': as duas coisas precisam ser verdade. Ex: 'preciso de dinheiro E tempo'.
or = 'OU': basta uma ser verdade. Ex: 'posso ir de carro OU de onibus'.
not = 'NAO': inverte a situacao. Ex: 'se NAO estiver chovendo, vou sair'.


Resumo da Unidade II
Aritmeticos: + - * / // % **   — calculos matematicos
Relacionais: == != > < >= <=   — retornam True ou False
Logicos: and  or  not   — combinam comparacoes


UNIDADE III
Estrutura de Decisao
Ensinando o programa a fazer escolhas com if, elif e else


Na vida real, tomamos decisoes o tempo todo: se estiver chovendo, pego o guarda-chuva; senao, nao preciso. Em programacao, fazemos isso com estruturas de decisao. O Python usa if, elif e else para isso.
if — Se isso for verdade, faca aquilo
O if e a estrutura mais basica. Ele verifica se uma condicao e verdadeira e, se for, executa o bloco de codigo dentro dele. O bloco e identificado pela indentacao (recuo com 4 espacos ou Tab).
# Estrutura do if
if condicao:
    # codigo que roda se a condicao for True
    # (tudo com recuo de 4 espacos faz parte do if)

# Exemplo pratico
temperatura = 35

if temperatura > 30:
    print("Que calor! Beba agua.")
    print("Considere usar roupa leve.")

print("Esta linha sempre aparece.")  # fora do if




Importante: Indentacao e obrigatoria em Python
Python usa o recuo (indentacao) para definir blocos de codigo.
Tudo que estiver com recuo depois do if: pertence ao if.
O padrao e 4 espacos. Use sempre o mesmo recuo para evitar erros.
Esquecer a indentacao e um dos erros mais comuns!


if / else — Uma coisa OU outra
O else e o 'caso contrario'. Se a condicao do if for False, o Python executa o bloco do else. Sempre um dos dois sera executado — nunca os dois ao mesmo tempo.
nota = float(input("Digite a nota: "))

if nota >= 7:
    print("Parabens! Voce foi aprovado.")
else:
    print("Voce nao atingiu a media. Estude mais!")

# Se nota = 8.0: imprime 'Parabens! Voce foi aprovado.'
# Se nota = 5.0: imprime 'Voce nao atingiu a media...'


if / elif / else — Multiplas opcoes
Quando temos mais de dois casos possiveis, usamos elif (abreviacao de 'else if'). O Python verifica cada condicao em ordem, e executa o bloco do primeiro que for True. Se nenhuma for True, executa o else.
nota = float(input("Digite a nota: "))

if nota >= 9:
    situacao = "Excelente"
elif nota >= 7:
    situacao = "Aprovado"
elif nota >= 5:
    situacao = "Recuperacao"
else:
    situacao = "Reprovado"

print(f"Situacao: {situacao}")




Dica: A ordem dos elif importa muito
O Python testa as condicoes de cima para baixo e para na primeira verdadeira.
Se voce colocar nota >= 5 antes de nota >= 7, o aluno com nota 8 cairia em 'Recuperacao'.
Sempre ordene do mais restritivo (maior valor) para o menos restritivo.


Ifs aninhados — if dentro de if
Podemos colocar um if dentro de outro. Isso e util quando a segunda verificacao so faz sentido se a primeira for verdadeira. Cuidado com a indentacao!
idade = int(input("Sua idade: "))
tem_habilitacao = input("Tem habilitacao? (s/n): ")

if idade >= 18:
    print("Voce e maior de idade.")
    if tem_habilitacao == "s":
        print("Pode dirigir!")
    else:
        print("Precisa tirar habilitacao primeiro.")
else:
    print("Voce ainda e menor de idade.")


Expressao condicional (if em uma linha)
Python permite escrever um if/else simples em uma unica linha. E util para situacoes simples onde voce precisa atribuir um valor baseado em uma condicao.
# Forma longa
if nota >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

# Forma curta (expressao ternaria)
resultado = "Aprovado" if nota >= 7 else "Reprovado"

# Leia como: resultado recebe 'Aprovado' SE nota >= 7, SENAO 'Reprovado'


Resumo da Unidade III
if condicao:   — executa se True
elif outra_condicao:   — testa nova condicao se o if anterior foi False
else:   — executa se todas as condicoes acima foram False
Indentacao (4 espacos)   — define o que pertence ao bloco


UNIDADE IV
Laco de Repeticao
Automatizando tarefas repetitivas com for e while


Imagine que voce precisa exibir os numeros de 1 a 100 na tela. Escrever 100 print()s seria absurdo. Os lacos de repeticao resolvem isso: eles executam um bloco de codigo varias vezes, automaticamente.
O laco for — repeticoes com contagem definida
O for e usado quando voce sabe QUANTAS vezes quer repetir, ou quando quer percorrer cada item de uma sequencia (uma lista, um texto, etc.). Em cada repeticao, uma variavel assume o proximo valor da sequencia.
# Estrutura do for
for variavel in sequencia:
    # codigo que se repete

# Exemplo: exibir numeros de 1 a 5
for numero in range(1, 6):  # range(1, 6) gera: 1, 2, 3, 4, 5
    print(numero)

# Saida:
# 1
# 2
# 3
# 4
# 5


A funcao range() — gerando sequencias de numeros
Forma
O que gera
Exemplo
range(n)
0 ate n-1
range(5)  ->  0,1,2,3,4
range(i, f)
i ate f-1
range(2, 6)  ->  2,3,4,5
range(i, f, p)
i ate f-1, pulando de p
range(0, 10, 2)  ->  0,2,4,6,8
range(f, i, -1)
De f ate i+1 (decrescente)
range(5, 0, -1)  ->  5,4,3,2,1


# Tabuada do 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# Contagem regressiva
for i in range(10, 0, -1):
    print(i)
print("Fogo!")

# Percorrer um texto letra por letra
for letra in "Python":
    print(letra)


O laco while — repete enquanto uma condicao for verdadeira
O while e usado quando voce NAO sabe exatamente quantas vezes vai repetir. Ele continua executando o bloco enquanto a condicao for True. Quando a condicao se torna False, o laco para.
# Estrutura do while
while condicao:
    # codigo que repete
    # (a condicao deve mudar em algum momento!)

# Exemplo: pede numero ate o usuario digitar 0
numero = -1
while numero != 0:
    numero = int(input("Digite um numero (0 para sair): "))
    if numero != 0:
        print(f"Voce digitou: {numero}")
print("Programa encerrado.")




Atencao!: Loop infinito — o erro mais temido!
Se a condicao do while NUNCA se tornar False, o programa fica preso para sempre.
Sempre garanta que algo dentro do while vai eventualmente fazer a condicao ser False.
Exemplo de loop infinito: while True: print('socorro')  — nunca para!
Se acontecer, pressione Ctrl+C para forcar o encerramento.


break e continue — controlando o fluxo do laco
Dentro de um laco, voce pode usar break para saiar imediatamente ou continue para pular para a proxima repeticao sem executar o restante do bloco atual.
# break — sai do laco imediatamente
for numero in range(1, 101):
    if numero == 5:
        print("Encontrei o 5! Saindo...")
        break
    print(numero)
# Imprime: 1, 2, 3, 4, e depois 'Encontrei o 5! Saindo...'

# continue — pula esta iteracao, vai para a proxima
for numero in range(1, 11):
    if numero % 2 == 0:  # se for par...
        continue          # ...pula e vai para o proximo
    print(numero)         # so imprime os impares: 1,3,5,7,9




Dica: Quando usar for e quando usar while?
Use for quando souber o numero de repeticoes ou tiver uma lista para percorrer.
Use while quando a repeticao depende de uma condicao que muda conforme o usuario interage.
Menus de programa (repete ate o usuario escolher 'sair') sao classicos usos do while.


while True + break — o padrao de menu
Uma tecnica muito usada e criar um while True (loop infinito) e usar break para sair apenas quando o usuario escolher a opcao de saida. E o padrao classico para menus interativos.
while True:
    print("\n=== MENU ===")
    print("1 - Opcao A")
    print("2 - Opcao B")
    print("0 - Sair")
    escolha = input("Digite sua opcao: ")

    if escolha == "1":
        print("Voce escolheu A!")
    elif escolha == "2":
        print("Voce escolheu B!")
    elif escolha == "0":
        print("Ate logo!")
        break
    else:
        print("Opcao invalida. Tente novamente.")


Resumo da Unidade IV
for var in sequencia:   — repeticao com numero definido
range(i, f, p)   — gera uma sequencia de numeros
while condicao:   — repete enquanto for True
break   — sai do laco  |  continue   — pula para a proxima iteracao


UNIDADE V
Listas e Matrizes
Guardando varios valores em uma unica variavel


Ate agora, cada variavel guardava apenas um valor. Mas e se precisassemos guardar as notas de 30 alunos? Criar 30 variaveis seria impraticavel. As listas resolvem isso: elas guardam varios valores em uma unica variavel, organizados em sequencia.
Criando e acessando listas
Uma lista e criada com colchetes [ ]. Os valores ficam separados por virgula. Cada valor tem um indice (posicao), que comeca no 0, nao no 1. Para acessar um valor, use o nome da lista seguido do indice entre colchetes.
# Criando uma lista
frutas = ["maca", "banana", "uva", "manga"]
notas  = [8.5, 7.0, 9.2, 6.8]
mista  = ["Ana", 20, True, 9.5]  # listas podem ter tipos mistos
vazia  = []                         # lista sem nenhum elemento

# Acessando por indice (comeca no 0!)
print(frutas[0])   # maca   (primeiro elemento)
print(frutas[1])   # banana (segundo elemento)
print(frutas[3])   # manga  (quarto elemento)
print(frutas[-1])  # manga  (ultimo elemento — indice negativo!)
print(frutas[-2])  # uva    (penultimo elemento)




Conceito: Indice negativo em Python
Python permite indices negativos para acessar elementos do final da lista.
-1 e o ultimo, -2 e o penultimo, e assim por diante.
Isso e muito util e exclusivo de Python — guarde essa dica!


Principais metodos de lista
Os metodos sao funcoes que pertencem a lista e permitem manipula-la de diversas formas. Voce chama um metodo escrevendo o nome da lista, um ponto e o nome do metodo.
Metodo / Funcao
O que faz
Exemplo
append(valor)
Adiciona ao final
frutas.append('pera')
insert(i, valor)
Insere na posicao i
frutas.insert(1, 'kiwi')
remove(valor)
Remove a primeira ocorrencia
frutas.remove('banana')
pop(i)
Remove e retorna o item na posicao i
frutas.pop(0)
pop()
Remove e retorna o ultimo
frutas.pop()
sort()
Ordena em ordem crescente
notas.sort()
reverse()
Inverte a ordem
frutas.reverse()
index(valor)
Retorna o indice do valor
frutas.index('uva')
count(valor)
Conta quantas vezes aparece
notas.count(7.0)
len(lista)
Retorna o tamanho da lista
len(frutas)
valor in lista
Verifica se o valor esta na lista
'maca' in frutas


nomes = ["Carlos", "Ana", "Bruno"]

nomes.append("Diana")       # ['Carlos', 'Ana', 'Bruno', 'Diana']
nomes.insert(1, "Eva")      # ['Carlos', 'Eva', 'Ana', 'Bruno', 'Diana']
nomes.remove("Bruno")       # ['Carlos', 'Eva', 'Ana', 'Diana']

print(len(nomes))           # 4
print("Ana" in nomes)       # True
print(nomes.index("Ana"))   # 2

nomes.sort()                # ['Ana', 'Carlos', 'Diana', 'Eva']
print(nomes)


Percorrendo listas com for
A forma mais natural de trabalhar com listas e combina-las com o for. O for percorre cada elemento automaticamente, sem precisar usar indices.
notas = [8.5, 7.0, 9.2, 6.8, 5.5]

# Percorrer e exibir cada item
for nota in notas:
    print(nota)

# Calcular a media
soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
print(f"Media: {media:.2f}")

# Forma moderna: funcoes sum() e len()
media = sum(notas) / len(notas)




Dica: Funcoes uteis para listas numericas
sum(lista)  — soma todos os elementos
max(lista)  — retorna o maior valor
min(lista)  — retorna o menor valor
len(lista)  — retorna a quantidade de elementos
sorted(lista) — retorna uma nova lista ordenada (sem alterar a original)


Fatiamento (slicing) — partes da lista
Voce pode pegar uma parte de uma lista usando fatiamento. A sintaxe e lista[inicio:fim], onde o fim NAO e incluido.
letras = ['a', 'b', 'c', 'd', 'e', 'f']

print(letras[1:4])    # ['b', 'c', 'd']  (indices 1, 2, 3)
print(letras[:3])     # ['a', 'b', 'c']  (do inicio ate 2)
print(letras[3:])     # ['d', 'e', 'f']  (do 3 ate o final)
print(letras[::2])    # ['a', 'c', 'e']  (de 2 em 2)
print(letras[::-1])   # ['f', 'e', 'd', 'c', 'b', 'a']  (invertido!)


Matrizes — listas dentro de listas
Uma matriz (ou lista de listas) e uma lista onde cada elemento tambem e uma lista. E o equivalente de uma tabela com linhas e colunas. Para acessar um elemento, use dois indices: [linha][coluna].
# Matriz 3x3 (3 linhas, 3 colunas)
matriz = [
    [1, 2, 3],   # linha 0
    [4, 5, 6],   # linha 1
    [7, 8, 9]    # linha 2
]

print(matriz[0][0])  # 1  (linha 0, coluna 0)
print(matriz[1][2])  # 6  (linha 1, coluna 2)
print(matriz[2][1])  # 8  (linha 2, coluna 1)

# Percorrendo toda a matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # quebra de linha ao fim de cada linha


Resumo da Unidade V
lista = [v1, v2, v3]   — cria uma lista
lista[i]   — acessa pelo indice (comeca no 0, -1 = ultimo)
append  remove  insert  pop  sort   — metodos principais
for item in lista:   — percorre cada elemento
sum()  max()  min()  len()   — funcoes uteis para listas


UNIDADE VI
Funcoes
Organizando, reutilizando e simplificando o seu codigo


Imagine escrever a receita de um bolo. Depois de escrita, voce pode fazer o bolo quantas vezes quiser so seguindo a receita — sem reescreve-la. Funcoes em programacao funcionam exatamente assim: voce escreve um bloco de codigo uma vez, da um nome a ele, e pode usa-lo quantas vezes quiser.
O que e uma funcao?
Uma funcao e um bloco de codigo com um nome, que realiza uma tarefa especifica. Quando voce quer executar essa tarefa, basta chamar a funcao pelo nome. Voce ja usou funcoes o tempo todo: print(), input(), int(), len() — todas sao funcoes!


Conceito: Por que usar funcoes?
Reutilizacao: escreva uma vez, use varias vezes.
Organizacao: divide o programa em partes menores e mais faceis de entender.
Manutencao: se precisar corrigir algo, corrige em um so lugar.
Legibilidade: o codigo fica mais limpo e facil de ler.


Criando uma funcao com def
Para criar uma funcao em Python, use a palavra-chave def, seguida do nome da funcao, parenteses e dois-pontos. O corpo da funcao deve estar indentado.
# Definindo a funcao
def saudacao():
    print("Ola! Bem-vindo ao sistema.")
    print("Tenha um otimo dia!")

# Chamando a funcao (pode chamar quantas vezes quiser)
saudacao()   # executa o bloco acima
saudacao()   # executa de novo


Parametros — passando informacoes para a funcao
Parametros sao variaveis que a funcao recebe quando e chamada. Eles ficam dentro dos parenteses na definicao. Quando voce chama a funcao, passa os valores (chamados argumentos) que ela vai usar.
# Funcao com 1 parametro
def saudacao_personalizada(nome):
    print(f"Ola, {nome}! Bem-vindo.")

saudacao_personalizada("Ana")    # Ola, Ana! Bem-vindo.
saudacao_personalizada("Carlos") # Ola, Carlos! Bem-vindo.

# Funcao com 2 parametros
def exibir_info(nome, idade):
    print(f"{nome} tem {idade} anos.")

exibir_info("Bruno", 22)   # Bruno tem 22 anos.
exibir_info("Eva", 19)     # Eva tem 19 anos.




Conceito: Parametro vs Argumento
Parametro: e a variavel na DEFINICAO da funcao.  def soma(a, b):  — a e b sao parametros.
Argumento: e o valor que voce passa ao CHAMAR a funcao.  soma(3, 5)  — 3 e 5 sao argumentos.
Na pratica, muita gente usa os dois termos de forma intercambiavelmente.


return — a funcao devolvendo um resultado
Muitas funcoes precisam calcular algo e devolver o resultado para quem a chamou. Para isso, usamos return. Quando a funcao encontra o return, ela para de executar e devolve o valor indicado.
# Funcao que RETORNA um valor
def somar(a, b):
    resultado = a + b
    return resultado

# Guardando o retorno em uma variavel
total = somar(5, 3)
print(total)              # 8

# Usando o retorno diretamente
print(somar(10, 20))      # 30
print(somar(2, 2) * 3)    # 12  (4 * 3)

# Funcao com varios returns (mas so um executa por vez)
def classificar_nota(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"

situacao = classificar_nota(7.5)
print(situacao)   # Aprovado




Importante: Funcoes com e sem return
Funcoes SEM return: executam uma tarefa e nao devolvem nada. Ex: print().
Funcoes COM return: calculam algo e devolvem o resultado. Ex: len(), sum(), int().
Uma funcao sem return devolve None (nada) automaticamente.


Parametros com valor padrao
Voce pode definir um valor padrao para um parametro. Se o argumento nao for passado ao chamar a funcao, ela usa o valor padrao automaticamente.
def saudacao(nome, periodo="dia"):
    print(f"Bom {periodo}, {nome}!")

saudacao("Ana")             # Bom dia, Ana!  (usa o padrao)
saudacao("Bruno", "tarde")  # Boa tarde, Bruno!  (substitui o padrao)
saudacao("Carlos", "noite") # Boa noite, Carlos!


Escopo — onde as variaveis existem
Variaveis criadas DENTRO de uma funcao so existem dentro dela (escopo local). Variaveis criadas FORA de todas as funcoes existem em todo o programa (escopo global).
def minha_funcao():
    variavel_local = 42   # existe so aqui dentro
    print(variavel_local) # funciona

minha_funcao()
# print(variavel_local)  <- ERRO! A variavel nao existe aqui fora

variavel_global = "oi"   # existe em todo o programa

def outra_funcao():
    print(variavel_global) # funciona — pode LER variaveis globais




Dica: Boa pratica com escopo
Prefira passar valores como parametros a usar variaveis globais dentro das funcoes.
Funcoes que so usam seus parametros sao mais faceis de testar e reutilizar.


Exemplo completo — tudo junto
Veja como organizar um programa usando funcoes para cada responsabilidade. Esse e o estilo de codigo que voce vai usar no projeto integrador.
# Cada funcao tem uma responsabilidade clara

def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"

def exibir_resultado(nome, media, situacao):
    print(f"Aluno: {nome}")
    print(f"Media: {media:.2f}")
    print(f"Situacao: {situacao}")

# Programa principal — usa as funcoes acima
nome = input("Nome do aluno: ")
notas = []
for i in range(1, 4):
    nota = float(input(f"Nota {i}: "))
    notas.append(nota)

media = calcular_media(notas)
situacao = classificar(media)
exibir_resultado(nome, media, situacao)


Resumo da Unidade VI
def nome_funcao(param1, param2):   — define uma funcao
nome_funcao(arg1, arg2)   — chama (executa) a funcao
return valor   — devolve um resultado para quem chamou
def f(p=padrao):   — parametro com valor padrao


