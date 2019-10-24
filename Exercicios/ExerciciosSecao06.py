from random import randint
# pip install num2words
from num2words import num2words

"""
# 1
i = 0
num = 1
while i < 5:
    if num % 3 == 0:
        print(f"{num} é múltiplo de 3")
        i += 1
    num += 1

# 2
for i in range(1, 101):
    print(i)

i = 1
while i <= 100:
    print(i)
    i += 1

# 3
i = 10
while i >= 0:
    print(i)
    i -= 1
print("Fim")

# 4
for i in range(0, 100_001, 1000):
    print(i)

# 5
soma = 0
for i in range(0, 10):
    valor = int(input("Digite um número: "))
    soma += valor
print(f"A soma dos valores digitados é {soma}")

# 6
soma = 0
for i in range(1, 11):
    valor = int(input("Digite um número: "))
    soma += valor
print(f"A média dos valores digitados é {soma / i}")

# 7
soma = 0
for i in range(1, 11):
    valor = int(input("Digite um número: "))
    while valor < 0:
        valor = int(input("Valor inválido.\nDigite um novo número: "))
    soma += valor
print(f"A média dos valores digitados é {soma / i}")

# 8
valor = int(input("Digite um número: "))
maior = menor = valor
for i in range(0, 9):
    valor = int(input("Digite um número: "))
    if valor > maior:
        maior = valor;
    elif valor < menor:
        menor = valor
print(f"O maior valor digitado foi {maior}")
print(f"O menor valor digitado foi {menor}")

# 9
n = int(input("Digite um número: "))
for i in range(0, n+1):
    if i % 2 == 1:
        print(i)

# 10
soma = 0
i = 0
j = 1
while i < 50:
    if j % 2 == 0:
        soma += j
        i += 1
    j += 1
print(f"A soma dos primeiros 50 números pares é {soma}")

# 11
n = int(input("Digite um número: "))
while n < 0:
    n = int(input("Valor inválido.\nDigite um novo número: "))
for i in range(0, n+1):
    print(i)

# 12
n = int(input("Digite um número: "))
while n < 0:
    n = int(input("Valor inválido.\nDigite um novo número: "))
for i in range(n, -1, -1):
    print(i)

# 13
n = int(input("Digite um número inteiro positivo e par: "))
while n < 0 or n % 2 == 1:
    n = int(input("Valor inválido.\nDigite um novo número: "))
for i in range(0, n+1, 2):
    print(i)

# 14
n = int(input("Digite um número inteiro positivo e par: "))
while n < 0 or n % 2 == 1:
    n = int(input("Valor inválido.\nDigite um novo número: "))
for i in range(n, -1, -2):
    print(i)

# 15
n = int(input("Digite um número inteiro positivo e ímpar: "))
while n < 0 or n % 2 == 0:
    n = int(input("Valor inválido.\nDigite um novo número: "))
for i in range(1, n+1, 2):
    print(i)

# 16
n = int(input("Digite um número inteiro positivo e ímpar: "))
while n < 0 or n % 2 == 0:
    n = int(input("Valor inválido.\nDigite um novo número: "))
for i in range(n, -1, -2):
    print(i)

# 17
n = int(input("Digite um número inteiro positivo: "))
soma = 0
while n < 0:
    n = int(input("Valor inválido.\nDigite um novo número: "))
for i in range(0, n+1):
    soma += i
print(f"A soma dos valores naturais até {n} é {soma}")

# 18
total = int(input("Digite a quantidade de números a ser lido: "))
n = int(input("Digite um número inteiro: "))
maior = n
quant = 1
for i in range(1, total):
    n = int(input("Digite um número inteiro: "))
    if n == maior:
        quant += 1
    elif n > maior:
        maior = n
        quant = 1
print(f"O maior número digitado foi {maior}, o qual foi digitado {quant} vezes")

# 19
n = int(input("Digite um número inteiro entre 100 e 999: "))
while n < 100 or n > 999:
    n = int(input("Valor inválido.\nDigite um novo número entre 100 e 999: "))
print(f"O número {n} é composto pelos algarismos {n//100}, {n % 100 // 10} e {n % 100 % 10 }")
# ou
#n = str(n)
#print(f"O número {n} é composto pelos algarismos {n[0]}, {n[1]} e {n[2]}")

# 20
n = int(input("Digite um número inteiro: "))
cont = 0
cont_par = 0
while n != 1000:
    if n % 2 == 0:
        cont_par += 1
    cont += 1
    n = int(input("Digite um número inteiro: "))
print(f"Foram digitados {cont} números (excluíndo o número 1000).\nDesses, {cont_par} eram pares")

# 21
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
soma = 0
produto = 1
for i in range(menor, maior+1):
    if i % 2 == 0:
        soma += i
    else:
        produto *= i
print(f"A soma dos números pares é {soma}")
print(f"O produto dos números ímpares é {produto}")

# 22
nota = float(input("Digite a nota do aluno: "))
cont = 0
soma = 0
while 10 <= nota <= 20:
    soma += nota
    cont += 1
    nota = float(input("Digite a nota do aluno: "))
print(f"A média do aluno é {soma / cont:.1f}")

# 23
n = int(input("Digite um número inteiro: "))
print(f"Os divisores de {n} são: ", end="")
for i in range(1, n+1):
    if i == n:
        print(i)
    elif n % i == 0:
        print(f"{i}, ", end="")

# 24
n = int(input("Digite um número inteiro: "))
soma = 0
for i in range(1, n):
    if n % i == 0:
        soma += i
print(f"A soma dos divisores de {n} (excluindo ele próprio) é: {soma}")

# 25
soma = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print(soma)

# 26
n = int(input("Digite um número inteiro: "))
i = n + 1
while i % 11 != 0 and i % 13 != 0 and i % 17 != 0:
    i += 1
print(f"O próximo número múltiplo de 11, 13 ou 17 é {i}")

# 27
n = int(input("Digite um número inteiro positivo: "))
while n < 0:
    n = int(input("Valor inválido.\nDigite um novo número: "))
soma = 1
for i in range(2, n+1):
    soma += 1/n
print(f"H({n}) = {soma}")

# 28
n = int(input("Digite um número inteiro positivo: "))
while n < 0:
    n = int(input("Valor inválido.\nDigite um novo número: "))
soma = 1
for i in range(1, n+1):
    fat = 1
    for j in range(i, 1, -1):
        fat *= j
    soma += 1/fat
print(f"E({n}) = {soma}")

# 29
soma = 0
num = 1
den = 2
quant_termos = int(input("Digite a quantidade de termos: "))
for _ in range(1, quant_termos):
    fat = 1
    for j in range(den, 1, -1):
        fat *= j
    soma += num/fat
    num += 1
    den += 2
print(soma)

# 30
n = int(input("Digite o valor de n: "))
soma = 0
for i in range(1, n+1):
    soma += i
print(f"1ª sequência: {soma}")

soma = 0
for i in range(1, 2*n):
    if i % 2 == 0:
        soma -= i
    else:
        soma += i
print(f"2ª sequência: {soma}")

soma = 0
for i in range(1, 2*n, 2):
    soma += i
print(f"3ª sequência: {soma}")

# 31
soma = 0
num = 1
den = 1
for _ in range(0, 50):
    soma += num / den
    num += 2
    den += 1
print(soma)

# 32
n = int(input("Quantas vezes quer lançar os dados? "))
for _ in range(0, n):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    if d1 > d2:
        print(f"D1: {d1} > D2: {d2}")
    elif d2 > d1:
        print(f"D2: {d2} > D1: {d1}")
    else:
        print(f"D1: {d1} = D2: {d2}")

# 33
n = int(input("Quantidade de múltiplos? "))
i = int(input("Digite i: "))
j = int(input("Digite j "))
cont = 0
valor = 0
while cont < n:
    if valor % i == 0 or valor % j == 0:
        if cont + 1 == n:
            print(valor)
        else:
            print(valor, end=", ")
        cont += 1
    valor += 1

# 34
valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))
valor = valor_final
while True:
    cont = 0
    for i in range(valor_inicial, valor_final+1):
        if valor % i == 0:
            cont += 1
        else:
            break
    if cont == valor_final - valor_inicial + 1:
        print(valor)
        break
    else:
        valor += 1

# 35
valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))
if valor_final < valor_inicial:
    print("Intervalo de valores inválido")
else:
    soma = 0
    for i in range(valor_inicial, valor_final+1):
        if i % 2 == 1:
            soma += i
    print(f"Soma dos ímpares no intervalo entre {valor_inicial} e {valor_final}: {soma}")

# 36
soma_quad = 0
soma_n = 0
for i in range(1, 101):
    soma_n += i
    soma_quad += i**2
soma_n **= 2
print(f"A diferença entre o quadrado da soma e a soma dos quadrados é {soma_n - soma_quad}")

# 37
for i in range(1000, 10000):
    x = int(str(i)[0:2])
    y = int(str(i)[2:4])
    if i == (x + y)**2:
        print(i)

# 38
for a in range(0, 1001):
    for b in range(0, 1001 - a):
        for c in range(0, 1001 - a - b):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print(f"a = {a}, b = {b} e c = {c}")

# 39
base = float(input("Digite a base do triângulo: "))
while base <= 0:
    base = float(input("Base inválida. Digite um novo valor para a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
while altura <= 0:
    altura = float(input("Altura inválida. Digite um novo valor para a altura do triângulo: "))

area = base * altura / 2
print(f"A área do triângulo é {area}")

# 40
n = int(input("Digite um número: "))
menor = maior = n
while n >= 0:
    if n < menor:
        menor = n
    elif n > maior:
        maior = n
    n = int(input("Digite um número: "))
print(f"Menor valor = {menor}")
print(f"Maior valor = {maior}")

# 41
r1 = float(input("Digite o valor de R1: "))
r2 = float(input("Digite o valor de R2: "))
while r1 > 0 and r2 > 0:
    print((r1*r2) / (r1+r2))
    r1 = float(input("Digite o valor de R1: "))
    r2 = float(input("Digite o valor de R2: "))

# 42
n = float(input("Digite um valor: "))
while n > 0:
    print(f"O quadrado de {n} é {n**2}")
    print(f"O cubo de {n} é {n**3}")
    print(f"A raíz quadrada de {n} é {n**(1/2)}")
    n = float(input("Digite um valor: "))

# 43
idade = int(input("Digite a idade: "))
soma = cont = 0
while idade > 0:
    soma += idade
    cont += 1
    idade = int(input("Digite a idade: "))
print(f"A média da idade é {soma / cont:.2f}")

# 44
n = int(input("Digite um número inteiro positivo: "))
while n < 0:
    n = int(input("Valor inválido.\nDigite um novo número: "))
a = 0
b = 1
print(f"{a} {b} ", end="")
while b < n:
    soma = a + b
    print(f"{soma} ", end="")
    a = b
    b = soma

# 45
opcao = input("(1) km/h para m/s\n(2) m/s para km/h\n(3) Finalizar\nOpção: ")
while opcao != "3":
    if opcao == "1":
        velocidade = float(input("Digite a velocidade em km/h: "))
        print(f"{velocidade} km/h equivale a {velocidade / 3.6} m/s")
    elif opcao == "2":
        velocidade = float(input("Digite a velocidade em m/s: "))
        print(f"{velocidade} m/s equivale a {velocidade * 3.6} km/h")
    else:
        print("Opção inválida")
    opcao = input("(1) km/h para m/s\n(2) m/s para km/h\n(3) Finalizar\nOpção: ")

# 46
n = randint(1, 1000)
valor = int(input("Qual número foi gerado? "))
cont = 1
while valor != n:
    if valor < n:
        print(f"O valor {valor} é menor do que o número gerado")
    elif valor > n:
        print(f"O valor {valor} é maior do que o número gerado")
    valor = int(input("Qual número foi gerado? "))
    cont += 1
print(f"Você acertou na {cont}ª tentativa")

# 47
opcao = input("(1) adição\n(2) subtração\n(3) multiplicação\n(4) divisão\n(5) Finalizar\nOpção: ")
while opcao != "5":
    if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
        n1 = float(input("Digite o 1º número: "))
        n2 = float(input("Digite o 2º número: "))
    if opcao == "1":
        print(f"{n1} + {n2} = {n1 + n2}")
    elif opcao == "2":
        print(f"{n1} - {n2} = {n1 - n2}")
    elif opcao == "3":
        print(f"{n1} * {n2} = {n1 * n2}")
    elif opcao == "4":
        print(f"{n1} / {n2} = {n1 / n2}")
    else:
        print("Opção inválida")
    opcao = input("(1) adição\n(2) subtração\n(3) multiplicação\n(4) divisão\n(5) Finalizar\nOpção: ")

# 48
a = 0
b = 1
prox = 0
soma = 0
print(f"{a} {b} ", end="")
while prox < 4_000_000:
    prox = a + b
    a = b
    b = prox
    if prox % 2 == 0 and prox < 4_000_000:
        soma += prox
print(f"Soma dos pares da sequência de Fibonacci = {soma}")

# 49
carlos = 1000
joao = carlos / 3
mes = 0
while joao < carlos:
    mes += 1
    carlos *= 1.02
    joao *= 1.05
print(f"Quantidade de meses: {mes}")

# 50
chico = 1.5
ze = 1.1
mes = 0
while ze < chico:
    mes += 1
    chico += 0.02
    ze += 0.03
print(f"Quantidade de meses: {mes}")

# 51
salario = 2000
aumento = 0.015
ano_atual = int(input("Digite o ano atual: "))
for _ in range(1996, ano_atual+1):
    salario += salario * aumento
    aumento *= 2
print(f"Em {ano_atual} o salário do funcionário é R${salario:.2f}")

# 52
saque = int(input("Digite o valor do saque: R$"))
notas = [100, 50, 20, 10, 5, 2, 1]
for n in range(0, len(notas)):
    quant_notas = saque // notas[n]
    print(f'{quant_notas} notas de {notas[n]}')
    saque %= notas[n]

# 53
n = int(input("Digite um número inteiro positivo: "))
while n < 0:
    n = int(input("Valor inválido.\nDigite um novo número: "))
valor = 1
for i in range(1, n+1):
    for _ in range(0, i):
        print(f"{valor}\t", end="")
        valor += 1
    print()

# 54
n = int(input("Digite um número inteiro maior que 1: "))
while n <= 1:
    n = int(input("Valor inválido.\nDigite um novo número: "))
primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
        break
if primo:
    print(f"O número {n} é primo")
else:
    print(f"O número {n} não é primo")

# 55
n = int(input("Digite a quantidade de números: "))
while n < 1:
    n = int(input("Valor inválido.\nDigite um novo número: "))
cont = 0
valor = 2
soma = 0
while cont < n:
    primo = True
    for i in range(2, valor):
        if valor % i == 0:
            primo = False
            break
    if primo:
        soma += valor
        cont += 1
    valor += 1
print(soma)

# 56
valor = 2
soma = 0
while valor < 2_000_000:
    primo = True
    for i in range(2, valor):
        if valor % i == 0:
            primo = False
            break
    if primo:
        print(valor)
        soma += valor
    valor += 1
print(f"Soma = {soma}")

# 57
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
cont = 0
for valor in range(menor, maior+1):
    primo = True
    for i in range(2, valor):
        if valor % i == 0:
            primo = False
            break
    if primo:
        cont += 1
print(f"Existem {cont} número(s) primo(s) entre {menor} e {maior}")

# 58
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
soma = 0
for valor in range(menor, maior+1):
    primo = True
    for i in range(2, valor):
        if valor % i == 0:
            primo = False
            break
    if primo:
        soma += valor
print(f"A soma dos número(s) primo(s) entre {menor} e {maior} é {soma}")

# 59
habitantes = int(input("Digite a quantidade de habitantes: "))
kwh = float(input("Digite o valor do kwh: R$"))
consumo = float(input(f"Digite o consumo do habitante {i}: "))
codigo = int(input("Digite o código do consumidor: "))
maior = menor = soma = consumo
consumo1 = consumo2 = consumo3 = 0
for i in range(2, habitantes+1):
    consumo = float(input(f"Digite o consumo do habitante {i}: "))
    codigo = int(input("Digite o código do consumidor: "))
    while codigo < 1 or codigo > 3:
        codigo = int(input("Valor inválido. Digite o código do consumidor: "))
    soma += consumo
    if codigo == 1:
        consumo1 += consumo
    elif codigo == 2:
        consumo2 += consumo
    else:
        consumo3 += consumo
print(f"Maior consumo = {maior}")
print(f"Menor consumo = {menor}")
print(f"Média consumo = {soma / habitantes:.2f}")
print(f"Consumo categoria 1 = {consumo1}")
print(f"Consumo categoria 2 = {consumo2}")
print(f"Consumo categoria 3 = {consumo3}")

# 61
maior = 0
maior_i = maior_j = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        palindromo = i * j
        v = len(str(palindromo))//2
        if str(palindromo)[:v] == (str(palindromo)[-v:])[::-1]:
            if palindromo > maior:
                maior = palindromo
                maior_i = i
                maior_j = j
            break;
print(f"Maior palíndromo obtido a partir de dois números de três dígitos: {maior_i} * {maior_j} = {maior}")

# 62
total = ""
for n in range(1, 1001):
    num = num2words(n, lang='pt-BR')
    total += num.replace(' ', '')
    print(num)

print(f'Entre 1 e 1000 temos {len(total)} letras.')

"""