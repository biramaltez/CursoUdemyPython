import math
from random import randint
from datetime import datetime

"""
# 1
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
if num1 > num2:
    print("O 1º número é maior que o 2º")
elif num2 > num1:
    print("O 2º número é maior que o 1º")
else:
    print("Os números são iguais")

# 2
num = float(input("Digite um número: "))
if num >= 0:
    print(f"A raíz quadrada de {num} é {math.sqrt(num)}")
else:
    print("Número inválido")

# 3
num = float(input("Digite um número: "))
if num >= 0:
    print(f"A raíz quadrada de {num} é {math.sqrt(num)}")
else:
    print(f"O quadrado de {num} é {math.pow(num, 2)}")

# 4
num = float(input("Digite um número: "))
if num >= 0:
    print(f"O quadrado de {num} é {math.pow(num, 2)}")
    print(f"A raíz quadrada de {num} é {math.sqrt(num)}")

# 5
num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")

# 6
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num2 > num1:
    print(f"{num2} é maior que {num1}")
else:
    print("Os números são iguais")
print(f"A diferença entre os números é {abs(num1 - num2)}")

# 7
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num2 > num1:
    print(f"{num2} é maior que {num1}")
else:
    print("Números iguais")

# 8
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    print(f"A média do aluno é {(nota1 + nota2) / 2:.1f}")
else:
    print("Nota inválida")

# 9
salario = float(input("Digite o salário do funcionário: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))
if prestacao > salario * 0.2:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")

# 10
altura = float(input("Digite a altura: "))
if 0 < altura < 3:
    sexo = input("Digite o sexo (m/f): ")[0].lower()
    if sexo == "m":
        print(f"O peso ideal da pessoa é {72.7 * altura - 58:.1f} kg")
    elif "f" == sexo:
        print(f"O peso ideal da pessoa é {62.1 * altura - 44.7:.1f} kg")
    else:
        print("Sexo inválido")
else:
    print("Altura inválida")

# 11
num = input("Digite um número: ")
if num.isdecimal() and int(num) > 0:
    print(f"A soma dos dígitos de {num} é {sum(map(int, num))}")
else:
    print("Valor inválido")

# 12
num = int(input("Digite um número: "))
if num < 0:
    print("Número inválido")
else:
    base = int(input("Digite a base para cálculo do logaritmo: "))
    print(f"O logaritmo de {num} na base {base} é {math.log(num, base)}")

# 13
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
peso1 = peso2 = 1
peso3 = 2
media = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)
print(f"A média é {media:.1f}")
if media >= 60:
    print("O aluno foi aprovado")
else:
    print("O aluno foi reprovado")

# 14
nota1 = float(input("Digite a 1ª nota (trabalho de laboratório): "))
if 0 <= nota1 <= 10:
    peso1 = 2
    nota2 = float(input("Digite a 2ª nota (avaliação semestral): "))
    if 0 <= nota2 <= 10:
        peso2 = 3
        nota3 = float(input("Digite a 3ª nota (exame final): "))
        if 0 <= nota3 <= 10:
            peso3 = 5
            media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
            print(f"A média é {media:.1f}")
            if media < 3:
                print("Aluno reprovado")
            elif media < 5:
                print("Aluno em recuperação")
            else:
                print("Aluno aprovado")
        else:
            print("Nota inválida")
    else:
        print("Nota inválida")
else:
    print("Nota inválida")

# 15
dia = int(input("Digite o dia da semana: "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Valor inválido")

# 16
mes = int(input("Digite o mês: "))
if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Valor inválido")

# 17
altura = float(input("Digite a altura: "))
if altura > 0:
    base_maior = float(input("Digite a base maior: "))
    if base_maior > 0:
        base_menor = float(input("Digite a base menor: "))
        if base_menor > 0:
            area = ((base_maior + base_menor) * altura) / 2
            print(f"A área do trapézio é {area}")
        else:
            print("Valor inválido")
    else:
        print("Valor inválido")
else:
    print("Valor inválido")

# 18
operacao = input("Digite a operação desejada (+, -, *, /): ")
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
if operacao == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operacao == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operacao == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operacao == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Operação inválida")

# 19
num = int(input("Digite um número: "))
if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0):
    print("Valor válido")
else:
    print("Valor inválido")
    
# 20
lado1 = float(input("Digite o valor do 1º lado: "))
lado2 = float(input("Digite o valor do 2º lado: "))
lado3 = float(input("Digite o valor do 3º lado: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("Triângulo equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é um triângulo")

# 21
opcao = input("Escolha a opção:\n"
              "1 - Soma de 2 números.\n"
              "2 - Diferença entre 2 números (maior pelo menor).\n"
              "3 - Produto entre 2 números.\n"
              "4 - Divisão entre 2 números (o denominador não pode ser zero).\n"
              "Opção: ")
if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))
    if opcao == "1":
        print(f"A soma de {num1} e {num2} é {num1 + num2}")
    elif opcao == "2":
        if num1 > num2:
            maior = num1
            menor = num2
        else:
            maior = num2
            menor = num1
        print(f"A subtração de {maior} e {menor} é {maior - menor}")
    elif opcao == "3":
        print(f"A produto entre {num1} e {num2} é {num1 * num2}")
    else:
        if num2 != 0:
            print(f"A divisão entre {num1} e {num2} é {num1 / num2}")
        else:
            print("O denominador não pode ser zero")
else:
    print("Opção inválida")

# 22
idade = int(input("Digite a idade: "))
if idade >= 65:
    print("O funcionário PODE se aposentar!")
else:
    tempo_servico = int(input("Digite o tempo de serviço: "))
    if tempo_servico >= 30:
        print("O funcionário PODE se aposentar!")
    elif idade >= 60 and tempo_servico >= 25:
        print("O funcionário PODE se aposentar!")
    else:
        print("O funcionário NÃO PODE se aposentar!")

# 23
ano = int(input("Digite o ano: "))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print(f"O ano {ano} É bissexto")
else:
    print(f"O ano {ano} NÃO É bissexto")

# 24
valor = float(input("Digite o valor do produto: "))
estado = input("Digite a sigla do estado: ").upper()
if estado == "MG":
    print(f"Preço final para {estado}: R${valor * 1.07:.2f}")
elif estado == "SP":
    print(f"Preço final para {estado}: R${valor * 1.12:.2f}")
elif estado == "RJ":
    print(f"Preço final para {estado}: R${valor * 1.15:.2f}")
elif estado == "MS":
    print(f"Preço final para {estado}: R${valor * 1.08:.2f}")
else:
    print("Estado inválido")

# 25
a = float(input('Digite o valor de "a": '))
b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))
if a == 0:
    print("Não é equação de 2º grau")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não existe raiz")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        if delta == 0:
            print(f"Raíz única: {raiz1}")
        else:
            raiz2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"Raízes: {raiz1} e {raiz2}")

# 26
distancia = float(input("Digite a distância: "))
litros = float(input("Digite a quantidade de litros consumidos: "))
consumo = distancia / litros
print(f"Consumo do carro: {consumo:.2f}")
if consumo < 8:
    print("Venda o carro!")
elif consumo < 14:
    print("Econômico")
else:
    print("Super econômico")

# 27
idade = int(input("Digite a idade do nadador: "))
if 5 <= idade <= 7:
    print("Categoria: Infantil A")
elif 8 <= idade <= 10:
    print("Categoria: Infantil B")
elif 11 <= idade <= 13:
    print("Categoria: Juvenil A")
elif 14 <= idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Categoria: Sênior")
else:
    print("Ainda não possui uma categoria")

# 28
x = int(input("Digite o 1º número: "))
y = int(input("Digite o 2º número: "))
z = int(input("Digite o 3º número: "))
opcao = input("Digite uma opção:\n"
              "(a) Geométrica\n"
              "(b) Ponderada\n"
              "(c) Harmônica\n"
              "(d) Aritmética\n"
              "Opção: ").lower()
if opcao == "a":
    print(f"Geométrica: {(x*y*z)**1/3}")
elif opcao == "b":
    print(f"Ponderada: {(x + 2*y + 3*z)/6}")
elif opcao == "c":
    print(f"Harmônica: {1 / (1/x + 1/y + 1/z)}")
elif opcao == "d":
    print(f"Aritmética: {(x + y + z) / 3}")
else:
    print("Opção inválida")

# 29
a = randint(1, 100)
b = randint(1, 100)
resultado = int(input(f"Qual a soma de {a} e {b}?\n"))
if resultado == a + b:
    print("Parabéns! Você acertou!")
else:
    print(f"Infelizmente a resposta não está correta. O correto seria {a + b}.")
    
# 30
x = int(input("Digite o 1º número: "))
y = int(input("Digite o 2º número: "))
z = int(input("Digite o 3º número: "))

if x < y and x < z:
    if y < z:
        print(f"{x} < {y} < {z}")
    else:
        print(f"{x} < {z} < {y}")
elif y < z:
    if x < z:
        print(f"{y} < {x} < {z}")
    else:
        print(f"{y} < {z} < {x}")
else:
    if x < y:
        print(f"{z} < {x} < {y}")
    else:
        print(f"{z} < {y} < {x}")

# 31
altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))
if 0 < altura < 1.2:
    if 0 < peso < 60:
        print("A")
    elif 60 <= peso <= 90:
        print("D")
    elif peso > 90:
        print("G")
elif 1.2 <= altura <= 1.7:
    if 0 < peso < 60:
        print("B")
    elif 60 <= peso <= 90:
        print("E")
    elif peso > 90:
        print("H")
elif altura > 1.7:
    if 0 < peso < 60:
        print("C")
    elif 60 <= peso <= 90:
        print("F")
    elif peso > 90:
        print("I")

# 32
codigo = int(input("Digite código do produto: "))
if 100 <= codigo <= 106:
    quantidade = int(input("Digite a quantidade desejada: "))
    if codigo == 100:
        preco = 1.2
    elif codigo == 101:
        preco = 1.3
    elif codigo == 102:
        preco = 1.5
    elif codigo == 103:
        preco = 1.2
    elif codigo == 104:
        preco = 1.7
    elif codigo == 105:
        preco = 2.2
    else:
        preco = 1.0
    print(f"O valor a ser pago é R${quantidade * preco:.2f}")
else:
    print("Código inválido")

# 33
valor_antigo = float(input("Digite o valor do produto: R$"))
valor_novo = 0
if 0 <= valor_antigo <= 50:
    valor_novo = valor_antigo * 1.05
elif 50 < valor_antigo <= 100:
    valor_novo = valor_antigo * 1.1
elif valor_antigo > 100:
    valor_novo = valor_antigo * 1.15

if 0 < valor_novo <= 80:
    print(f"O produto de valor R${valor_novo} é barato")
elif 80 < valor_novo <= 120:
    print(f"O produto de valor R${valor_novo} é normal")
elif 120 < valor_novo <= 200:
    print(f"O produto de valor R${valor_novo} é caro")
elif valor_novo > 200:
    print(f"O produto de valor R${valor_novo} é muito caro")
else:
    print("Valor inválido")

# 34
nota = float(input("Digite a nota do aluno: "))
falta = int(input("Digite a quantidade de faltas: "))
if 9 <= nota <= 10 and falta <= 20:
    print("Conceito A")
elif (9 <= nota <= 10 and falta > 20) or (7.5 <= nota < 9 and falta <= 20):
    print("Conceito B")
elif (7.5 <= nota < 9 and falta > 20) or (5 <= nota < 7.5 and falta <= 20):
    print("Conceito C")
elif (5 <= nota < 7.5 and falta > 20) or (4 <= nota < 5 and falta <= 20):
    print("Conceito D")
elif (4 <= nota < 5 and falta > 20) or (0 <= nota < 4):
    print("Conceito E")
else:
    print("Nota inválida")

# 35
data = input("Digite uma data no formato dd/mm/aaaa: ")
if len(data) == 10 and data[2:3] == "/" and data[5:6] == "/":
    ano = data[6:10]
    if ano.isdecimal() and int(ano) >= 0:
        ano = int(ano)
        if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
            bissexto = True
        else:
            bissexto = False
        mes = data[3:5]
        if mes.isdecimal():
            mes = int(mes)
            if 1 <= mes <= 12:
                dia = data[0:2]
                if dia.isdecimal():
                    dia = int(dia)
                    if (1 <= dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)) \
                            or (1 <= dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11)) \
                            or (1 <= dia <= 29 and mes == 2 and bissexto) \
                            or (1 <= dia <= 28 and mes == 2):
                        print("Data válida")
                    else:
                        print("Data inválida")
        else:
            print("Data inválida")
    else:
        print("Data inválida")
else:
    print("Data no formato inválido")

# 36
venda = float(input("Digite o valor da venda: R$"))
comissao = 0
if venda >= 100_000:
    comissao = 700 + venda*0.16
elif 80_000 <= venda < 100_000:
    comissao = 650 + venda*0.14
elif 60_000 <= venda < 80_000:
    comissao = 600 + venda*0.14
elif 40_000 <= venda < 60_000:
    comissao = 550 + venda*0.14
elif 20_000 <= venda < 40_000:
    comissao = 500 + venda*0.14
elif 0 <= venda < 20_000:
    comissao = 400 + venda*0.14

if comissao == 0:
    print("Valor de venda inválido")
else:
    print(f"A comissão paga ao vendedor é de R${comissao:.2f}")

# 37
chegada = input("Digite a hora de chegada no formato hh:mm --> ")
hora_chegada = chegada[0:2]
minuto_chegada = chegada[3:5]
if hora_chegada.isdecimal() and minuto_chegada.isdecimal() \
        and 0 <= int(hora_chegada) <= 23 and 0 <= int(minuto_chegada) <= 59:
    hora_chegada = int(hora_chegada)
    minuto_chegada = int(minuto_chegada)

    saida = input("Digite a hora de saída no formato hh:mm --> ")
    hora_saida = saida[0:2]
    minuto_saida = saida[3:5]
    if hora_saida.isdecimal() and minuto_saida.isdecimal() \
            and 0 <= int(hora_saida) <= 23 and 0 <= int(minuto_saida) <= 59:
        hora_saida = int(hora_saida)
        minuto_saida = int(minuto_saida)

        tempo = 0 # tempo de estacionamento em hora
        if hora_chegada < hora_saida:
            tempo = hora_saida - hora_chegada
            if minuto_saida > minuto_chegada:
                tempo += 1
        elif hora_chegada > hora_saida:
            tempo = 24 - hora_chegada + hora_saida
            if minuto_saida > minuto_chegada:
                tempo += 1
        else:
            if minuto_saida > minuto_chegada:
                tempo = 1
            else:
                tempo = 24

        print(f"Tempo de duração: {tempo} hora(s)")
        valor = 0
        if tempo == 1 or tempo == 2:
            valor = tempo * 1
        else:
            valor = 2
            if tempo == 3 or tempo == 4:
                tempo -= 2
                valor += tempo * 1.4
                tempo += 2
            else:
                valor = 4.8
                tempo -= 4
                valor += tempo * 2
        print(f"Total a ser pago: R${valor:.2f}")
    else:
        print("Horário de saída inválido")
else:
    print("Horário de chegada inválido")

# 38
data = input("Digite a data de nascimento no formato dd/mm/aaaa: ")
if len(data) == 10 and data[2:3] == "/" and data[5:6] == "/":
    ano = data[6:10]
    if ano.isdecimal() and int(ano) >= 0:
        ano = int(ano)
        if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
            bissexto = True
        else:
            bissexto = False
        mes = data[3:5]
        if mes.isdecimal():
            mes = int(mes)
            if 1 <= mes <= 12:
                dia = data[0:2]
                if dia.isdecimal():
                    dia = int(dia)
                    if (1 <= dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)) \
                            or (1 <= dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11)) \
                            or (1 <= dia <= 29 and mes == 2 and bissexto) \
                            or (1 <= dia <= 28 and mes == 2):
                        now = datetime.now()
                        print(f"Data atual: {now.day}/{now.month}/{now.year}")
                        if ano < now.year or (ano == now.year and mes < now.month) \
                                or (ano == now.year and mes == now.month and dia <= now.day):
                            print("Data válida")
                        else:
                            print("Data inválida")
                    else:
                        print("Data inválida")
        else:
            print("Data inválida")
    else:
        print("Data inválida")
else:
    print("Data no formato inválido")

# 39
salario = float(input("Digite o salário do funcionário: R$"))
tempo = int(input("Digite o tempo de serviço (en anos): "))
if salario <= 0 and tempo < 0:
    print("Valores inválidos")
else:
    reajuste = 0
    if salario <= 500:
        reajuste = salario * 0.25
    elif salario <= 1000:
        reajuste = salario * 0.2
    elif salario <= 1500:
        reajuste = salario * 0.15
    elif salario <= 2000:
        reajuste = salario * 0.1

    bonus = 0
    if 1 <= tempo <= 3:
        bonus = 100
    elif 4 <= tempo <= 6:
        bonus = 200
    elif 7 <= tempo <= 10:
        bonus = 300
    else:
        bonus = 500
    
    if reajuste == 0 and bonus == 0:
        print(f"O salário do funcionário não recebeu reajuste e continuará sendo R${salario}")
    else:
        print(f"O funcionário teve um reajuste de R${reajuste} e um bônus de R${bonus}."
              f"O novo salário do funcionário será {salario + reajuste + bonus}")

# 40
valor = float(input("Digite o custo de fábrica de um carro: R$"))
if valor < 0:
    print("Valor inválido")
else:
    comissao = 0
    imposto = 0
    if valor < 12_000:
        comissao = valor * 0.05
    elif valor <= 25_000:
        comissao = valor * 0.1
        imposto = valor * 0.15
    else:
        comissao = valor * 0.15
        imposto = valor * 0.2
    print(f"O carro custará R${valor + comissao + imposto}")

# 41
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / altura**2
print(f"O IMC é {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Peso em excesso")
elif imc < 35:
    print("Obeso Grau I")
elif imc < 40:
    print("Obeso Grau II (severa)")
else:
    print("Obeso Grau III (mórbida)")

"""