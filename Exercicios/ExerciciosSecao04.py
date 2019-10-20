import math

"""
# 1
num_int = int(input("Digite um número inteiro: "))
print(num_int)

# 2
num_real = float(input("Digite um número real: "))
print(num_real)

# 3
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
soma = num1 + num2 + num3;
print(f'A soma de {num1}, {num2} e {num3} é {soma}')

# 4
num_real = float(input("Digite um número real: "))
print(num_real ** 2)

# 5
num_real = float(input("Digite um número real: "))
print(num_real / 5)

# 6
temperatura_celsius = float(input("Digite a temperatura em ºC: "))
temperatura_fahrenheit = temperatura_celsius * (9/5) + 32
print(f"{temperatura_celsius}ºC corresponde a {temperatura_fahrenheit}ºF")

# 7
temperatura_fahrenheit = float(input("Digite a temperatura em ºF: "))
temperatura_celsius = 5 * (temperatura_fahrenheit - 32)/9
print(f"{temperatura_fahrenheit}ºF corresponde a {temperatura_celsius}ºC")

# 8
temperatura_kelvin = float(input("Digite a temperatura em Kelvin: "))
temperatura_celsius = temperatura_kelvin - 273.15
print(f"{temperatura_kelvin} Kelvin corresponde a {temperatura_celsius}ºC")

# 9
temperatura_celsius = float(input("Digite a temperatura em ºC: "))
temperatura_kelvin = temperatura_celsius + 273.15
print(f"{temperatura_celsius}ºC corresponde a {temperatura_kelvin} Kelvin")

# 10
velocidade = float(input("Digite a velocidade em km/h: "))
print(f"{velocidade} km/h equivale a {velocidade / 3.6} m/s")

# 11
velocidade = float(input("Digite a velocidade em m/s: "))
print(f"{velocidade} m/s equivale a {velocidade * 3.6} km/h")

# 12
distancia = float(input("Digite a distância em milhas: "))
print(f"{distancia} mi equivale a {1.61 * distancia} km")

# 13
distancia = float(input("Digite a distância em quilômetros: "))
print(f"{distancia} km equivale a {distancia / 1.61} mi")

#14
angulo = float(input("Digite o ângulo em graus: "))
print(f"{angulo} em grau equivale a {angulo * math.pi / 180} radianos")

#15
angulo = float(input("Digite o ângulo em radianos: "))
print(f"{angulo} em radiano equivale a {angulo * 180 / math.pi} graus")

#16
comprimento = float(input("Digite o comprimento em polegadas: "))
print(f"{comprimento} em polegada equivale a {comprimento * 2.54} cm")

#17
comprimento = float(input("Digite o comprimento em centímetros: "))
print(f"{comprimento} em cm equivale a {comprimento / 2.54} polegadas")

#18
volume = float(input("Digite o volume em m³: "))
print(f"{volume} m³ equivale a {1000 * volume} litros")

#19
volume = float(input("Digite o volume em litros: "))
print(f"{volume} litros equivale a {volume / 1000} m³")

#20
massa = float(input("Digite a massa em quilos: "))
print(f"{massa} kg equivale a {massa / 0.45} lb")

#21
massa = float(input("Digite a massa em lbras: "))
print(f"{massa} lb equivale a {massa * 0.45} kg")

#22
comprimento = float(input("Digite o comprimento em jardas: "))
print(f"{comprimento} em yd equivale a {0.91 * comprimento} m")

#23
comprimento = float(input("Digite o comprimento em metros: "))
print(f"{comprimento} em m equivale a {comprimento / 0.91} yd")

#24
area = float(input("Digite o comprimento em m²: "))
print(f"{area} em m² equivale a {area * 0.000247} acres")

#25
area = float(input("Digite o comprimento em acres: "))
print(f"{area} em acre equivale a {area * 4048.58} m²")

#26
area = float(input("Digite o comprimento em m²: "))
print(f"{area} em m² equivale a {area * 0.0001} hectares")

#27
area = float(input("Digite o comprimento em hectares: "))
print(f"{area} em hectare equivale a {area * 10_000} m²")

#28
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
soma = num1**2 + num2**2 + num3**2;
print(f'A soma dos quadrados de {num1}, {num2} e {num3} é {soma}')

#29
num1 = float(input("Digite a 1ª nota: "))
num2 = float(input("Digite a 2ª nota: "))
num3 = float(input("Digite a 3ª nota: "))
num4 = float(input("Digite a 4ª nota: "))
media = (num1+num2+num3+num4) / 4
print(f'A média de {num1}, {num2}, {num3} e {num4} é {media}')

#30
valor_real = float(input("Digite o valor em real: R$"))
cotacao = float(input("Digite o valor da cotação de 1 dólar: R$"))
print(f"R${valor_real} equivale a ${valor_real / cotacao}")

#31
num = int(input("Digite um valor inteiro: "))
print(f"Antecessor: {num-1}\nSucessor: {num+1}")

#32
num = int(input("Digite um valor inteiro: "))
a = num * 3 + 1
b = num * 2 - 1
print(f"Resultado = {a+b}")

#33
lado = float(input("Digite o valor do lado de um quadrado: "))
print(f"A área do quadrado de lado {lado} é {lado * lado}")

#34
raio = float(input("Digite o valor do raio do círculo: "))
print(f"A área do círculo de raio {raio} é {math.pi * raio ** 2}")

#35
cateto_a = float(input("Digite o valor do cateto A: "))
cateto_b = float(input("Digite o valor do cateto B: "))
print(f"O valor da hipotenusa do triângulos de catetos com valores "
      f"{cateto_a} e {cateto_b} é {math.sqrt(cateto_a**2 + cateto_b**2)}")

#36
altura = float(input("Digite o valor da altura do cilindo: "))
raio = float(input("Digite o valor do raio do cilindo: "))
volume = math.pi * raio**2 * altura
print(f"O volume do cilindro é {volume}")

#37
valor = float(input("Digite o valor do produto: "))
print(f"Com 12% de desconto, o produto custará {valor * 0.88}")

#38
salario = float(input("Digite o salário do funcionário: "))
print(f"Com 25% de aumento, o salário passa a ser {salario * 1.25}")

#39
valor = 780_000.0
ganhador1 = valor * 0.46
ganhador2 = valor * 0.32
ganhador3 = valor - ganhador1 - ganhador2
print(f"Ganhador 1: R${ganhador1}\nGanhador 2: R${ganhador2}\n"
      f"Ganhador 3: R${ganhador3}")

#40
dias = int(input("Digite a quantidade de dias trabalhados: "))
valor_dia = 30.0
print(f"Valor líquido a ser pago ao encanador: R${valor_dia * dias * 0.92}")

#41
valor_hora = float(input("Digite o valor da hora de trabalho: R$"))
horas = int(input("Digite o número de horas trabalhadas: "))
print(f"Será pago ao funcionário R${valor_hora*horas*1.1}")

#42
salario_base = float(input("Digite o salário base do funcionário: R$"))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
print(f"Salário a receber: R${salario_base + gratificacao - imposto}")

#43
valor = float(input("Digite o valor do produto: R$"))
valor_com_desconto = valor * 0.9
print(f"Caso pague com 10% de desconto, o valor será R${valor_com_desconto}")
print(f"Caso pague em 3x, o valor de cada parcela será R${valor / 3}")
print(f"Comissão do vendedor para pagamento à vista: R${valor_com_desconto * 0.05}")
print(f"Comissão do vendedor para pagamento parcelado: R${valor * 0.05}")

#44
altura_degrau = float(input("Digite a altura do degrau: "))
altura_desejada = float(input("Digite a altura que se deseja chegar: "))
print(f"Deve-se subir {int(math.ceil(altura_desejada / altura_degrau))} para chegar a altura desejada")

#45
letra = input("Digite uma letra: ")
letra = letra[0].upper()
# A função ord() devolve o código numérico do caractere passado como parâmetro.
# A função chr() devolve o caracter corresponde ao código numérico passado como parâmetro.
print(f"A letra {letra} em minúsculo é {chr(ord(letra) + 32)}")

#46
num = int(input("Digite um número: "))
num_invertido = int(str(num)[::-1])
print(f"{num} invertido é {num_invertido}")
print(type(num_invertido))

#47
# Verificar se dá para fazer sem repetição
numero = input('Informe um número inteiro de 4 dígitos: ')
for letra in numero:
    print(f'{letra}')

#48
segundo = int(input("Digite valor em segundos: "))
hora = segundo // 3600
minuto = (segundo - (hora * 3600)) // 60
s = segundo % 60
print(f"{segundo} s = {hora}:{minuto}:{s}")

#49
valor = input("Digite a hora no formato hh:mm:ss -> ")
hora = int(valor[0:2])
minuto = int(valor[3:5])
segundo = int(valor[6:8])
print(f"Hora inicial: {hora}:{minuto}:{segundo}")
duracao = int(input("Digite a duração do experimento (em s): "))
segundo += duracao
minuto += segundo // 60
segundo = int(segundo % 60)
hora += minuto // 60
minuto = int(minuto % 60)
print(f"Hora final: {hora}:{minuto}:{segundo}")

#50
ano_atual = int(input("Digite o ano atual: "))
idade = int(input("Digite a idade da pessoa: "))
print(f"A pessoa nasceu em {ano_atual - idade}")

#51
x = float(input("Digite o valor da coordenada X: "))
y = float(input("Digite o valor da coordenada Y: "))
dist = math.sqrt(x**2 + y**2)
print(f"A distância do ponto ({x}, {y}) para a origem (0, 0) é {dist}")

#52
amigo1 = float(input("Digite o valor apostado por 1: "))
amigo2 = float(input("Digite o valor apostado por 2: "))
amigo3 = float(input("Digite o valor apostado por 3: "))
premio = float(input("Digite o valor do prêmio: "))
total = amigo1 + amigo2 + amigo3
prop1 = amigo1 / total
prop2 = amigo2 / total
prop3 = amigo3 / total
print(f"O amigo 1 receberá R${premio * prop1:.2f}")
print(f"O amigo 2 receberá R${premio * prop2:.2f}")
print(f"O amigo 3 receberá R${premio * prop3:.2f}")

#53
comprimento = float(input("Digite o comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
valor_tela = float(input("Digite o valor do metro da tela: R$"))
print(f"Será necessário gastar R${comprimento * largura * valor_tela:.2f} para telar todo o terreno")

"""