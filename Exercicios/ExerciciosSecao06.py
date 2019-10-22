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

"""

# 23