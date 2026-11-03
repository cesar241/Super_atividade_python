'''
# 1. Ola, Mundo!
print("Ola, Mundo!")
'''

'''
# 2. Apresentacao
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

print("Meu nome é", nome, "tenho", idade, "anos e moro em", cidade)
'''

'''
# 3. Nome do usuario
nome = input("Digite o seu nome: ")

print("Ola,", nome, "!")
'''

'''
# 4. Idade do usuario
idade = int(input("Digite a sua idade: "))

print("Voce tem", idade, "anos.")
'''

'''
# 5. Soma simples
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

print("A soma é:", soma)
'''

'''
# 6. Quatro operacoes
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print("Soma:", soma)
print("Subtração:", sub)
print("Multiplicação:", mult)
print("Divisão:", div)
'''

'''
# 7. Dobro
num1 = int(input("Digite um número que será dobrado: "))

dobro = num1 * 2

print("Seu número dobrado é:", dobro)
'''

'''
# 8. Triplo e metade
num1 = int(input("Digite um número que será triplicado e terá sua metade calculada: "))

triplo = num1 * 3
metade = num1 / 2

print("O triplo do seu número é:", triplo)
print("A metade do seu número é:", metade)
'''

'''
# 9. Nome completo
nome = input("Digite o seu primeiro nome: ")
sobrenome = input("Digite o seu sobrenome: ")

print("Nome completo:", nome, sobrenome)
'''

'''
# 10. Ano de nascimento
ano_nascimento = int(input("Digite o ano que você nasceu: "))

idade2 = 2026 - ano_nascimento

print("Em 2026 você terá aproximadamente", idade2, "anos.")
'''

'''
# 11. Conversao de metros
metros = int(input("Digite uma medida em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print("Em centímetros:", centimetros)
print("Em milímetros:", milimetros)
'''

'''
# 12. Minutos para segundos
minutos = int(input("Digite uma quantidade de minutos: "))

segundos = minutos * 60

print(minutos, "minutos correspondem a", segundos, "segundos.")
'''

'''
# 13. Horas para minutos
horas = int(input("Digite uma quantidade de horas: "))

minutos = horas * 60

print(horas, "horas correspondem a", minutos, "minutos.")
'''

'''
# 14. Temperatura
celsius = int(input("Digite uma temperatura em graus Celsius: "))

fahrenheit = celsius * 9 / 5 + 32

print("A temperatura convertida para Fahrenheit é:", fahrenheit)
'''

'''
# 15. Conversão em Dolar
real = float(input("Digite um valor em real: "))
dolar = 5
dolares = real / dolar
print(f"sua quantidade é: US$ {dolares:.2f}")
'''

'''
# 16. Area do quadrado
quadrado = int(input("Digite a largura do seu quadrado: "))
area = quadrado * quadrado
print(f"sua area é {area}")
'''

'''
# 17. Area do retangulo
largura = int(input("Digite a base do seu retangulo: "))
altura = int(input("Digite a altura do seu retangulo: "))

area = largura * altura 

print(f"A area do seu retangulo é: {area}")
'''

'''
# 18. Area do triangulo
base = int(input("Digite a base do seu triangulo: "))
altura = int(input("Digite a altura do seu triangulo: "))

area = base * altura / 2

print(f"A area do seu triangulo é: {area}")
'''

'''
# 19. Area do circulo
raio = int(input("Digite o raio do seu circulo: "))

area = 3.14 * raio ** 2

print(f"A area do circulo é: {area}")
'''

'''
# 20. Perimetro do retangulo
largura = int(input("Digite a base do seu retangulo: "))
altura = int(input("Digite a altura do seu retangulo: "))

perimetro = 2 * (largura + altura)

print("O perímetro do retângulo é:", perimetro)
'''

'''
# 21. Media de tres notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Sua nota média é: {media:.2f}")
'''

'''
# 22. Salario por hora
horas = int(input("Digite quanto você ganha por Hora: "))
carga = int(input("Digite a sua carga de trabalho mensal: "))

bruto = horas * carga

print("seu sálario bruto é de", bruto, "R$")
'''

'''
# 23. Aumento salarial
salario = float(input("Digite o seu salario: "))

aumento = salario * 0.10
novo_salario = salario + aumento
print(f"seu salario era de R$ {salario:.2f}")
print(f"o aumento foi de R$ {aumento:.2f}")
print(f"o novo salario é R$ {novo_salario:.2f}")
'''

'''
# 24. Desconto
preco = float(input("Digite o preço de um produto: "))

desconto = preco * 0.15
precofinal = preco - desconto 

print(f"Valor do desconto (15%): R$ {desconto:.2f}")
print(f"preço final com desconto: R$ {precofinal:.2f}")
'''

'''
# 25. Parcelamento
total = float(input("Digite o valor total da compra: "))
parcelas = int(input("Digite o numero de parcelas: "))

valor_parcela = total / parcelas 

print(f"a sua compra foi dividida em {parcelas}x de R${valor_parcela:.2f} sem juros.")
'''

'''
# 26. IMC
peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura**2)

print(f"o seu IMC é {imc:.2f}")
'''

'''
# 27. Media ponderada
nota1 = float(input("Digite a sua primeira nota (Peso 2): "))
nota2 = float(input("Digite a sua segunda nota (Peso 3): "))

media_ponderada = (nota1 * 2 + nota2 * 3) / (2 + 3)

print(f"A media ponderada é: {media_ponderada:.2f}")
'''

'''
# 28. Resto da divisao
num1 = int(input("Digite o primeiro numero (Dividendo): "))
num2 = int(input("Digite o segundo numero (Divisor): "))

quociente = num1 // num2
resto = num1 % num2

print(f"quociente é: {quociente}")
print(f"Resto da divisão: {resto}")
'''

'''
# 29. Antecessor e sucessor
numero = int(input("Fale um numero inteiro e eu te mostrarei o seu antecessor e o sucessor: "))

antecessor = numero - 1
sucessor = numero + 1

print(f"o antecessor do seu numero é {antecessor}")
print(f"o sucessor do seu numero é {sucessor}")
'''

'''
# 30. Potencia
base = float(input("Fale uma base: "))
expoente = float(input("Fale um expoente: "))

resultado = base**expoente

print(f"A base {base} elevada a {expoente} é: {resultado}")
'''

'''
# 31. Positivo ou negativo
numero = float(input("Me de um numero e eu te falo se ele é positivo, negativo ou igual a zero: "))

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é igual a zero")
'''

'''
# 32. Maior de idade
idade = int(input("me fale a idade que eu te digo se é maior de idade ou não: "))

if idade >= 18:
    print("Você é de maior!")
else:
    print("Você é de menor")
'''

'''
# 33. Par ou impar
numero = int(input("Digite um numero inteiro: "))



if numero % 2 == 0:
    print("Seu numero é par")
else:
    print("Seu numero é impar")
'''

'''
# 34. Maior entre dois numeros
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else:
    print("Os números são iguais")
'''

'''
# 35. Maior entre tres numeros
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1 >= num2 and num1 >= num3:
    print("O maior número é o primeiro")
elif num2 >= num1 and num2 >= num3:
    print("O maior número é o segundo")
else:
    print("O terceiro número é o maior")
'''

'''
# 36. Menor entre tres numeros
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1 <= num2 and num1 <= num3:
    print("O menor número é o primeiro")
elif num2 <= num1 and num2 <= num3:
    print("O menor número é o segundo")
else:
    print("O menor número é o terceiro")
'''

'''
# 37. Aprovacao
media = float(input("Digite a media de notas do aluno: "))

if media >= 6:
    print("Aluno foi aprovado")
else:
    print("Aluno foi reprovado")
'''

'''
#38
media = float(input("Digite a media de notas do aluno: "))

if media >= 7:
    print("Aluno foi aprovado")
elif media >= 5:
    print("O aluno está de recuperação")
else:
    print("Aluno foi reprovado")
    '''

'''
#39
idade = int(input("Digite a sua idade: "))

if idade <= 11:
    print(f"você é uma criança")
elif idade <= 17:
    print(f"você é um adolescente")
elif idade <= 59:
    print(f"você é um adulto")
else:
    print("você é um idoso")
    '''

'''
#40
senha = int(input("Digite uma senha para entrar: "))

if senha == 2112:
    print("Acesso permitido")
else:
    print("Acesso negado")
    '''

'''
#41
usuario_correto = "César"
senha_correta = "César AMA a Shopia"

usuario = input("digite o usuario")
senha = input("Digite a senha para entrar: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login efetuado com sucesso")
else:
    print("Usuario ou senha incorretos.")

'''

'''
#42
numero = int(input("Digite um numero para saber se ele é multiplo de 5"))

if numero % 5 == 0:
    print("o numero é multiplo de 5")
else:
    print("o numero não é multiplo de 5")
    '''

'''
#43
numero = int(input("Digite um numero para saber se ele é divisivel de 5 e 3"))

if numero % 3 == 0 and numero % 5 == 0:
    print("O numero é divisivel por 3 e 5")
else:
    print("o numero não é divisivel")
    '''

'''
#44
ano = int(input("Digite um ano ai: "))

if ano % 4 == 0:
    print("bissexto")
else:
    print("não bissexto")
    '''

'''
#45
valor = int(input("Digite um valor para calcular quanto de desconto em reais terá (10% de desconto): "))
if valor > 200:
    desconto = valor * 0.10
    compra = desconto
    print(f"Desconto de {compra:.2f}")
else:
    print("Não tem desconto")
    '''

'''
#46
valor = int(input("Digite um valor: "))
frete = 20
if valor > 150:
    print(f"frete grátis")
else:

    print(f"Frete de {frete}")
    '''

'''
#47
num1 = int(input("Digite o primeiro numero "))

num2 = int(input("Digite o segundo numero "))

operacao = input("Digite a operação que você quer ")

adicao = num1 + num2
subtracao = num1 - num2
mult = num1 * num2

if operacao == "+":
    print(f"Deu {adicao}")

elif operacao == "-":
    print(f"Deu {subtracao}")

elif operacao == "*":
    print(f"{mult}")

elif operacao == "/":
    if num2 == 0:
        print("Seu número não pode ser dividido por 0")
    else:
        div = num1 / num2   
        print(f"{div}")

else:
    print("Sua operação não é valida")
'''

'''
#48
lado1 = int(input("De o primeiro lado do triangulo "))
lado2 = int(input("De o segundo lado do triangulo "))
lado3 = int(input("De o terceiro lado do triangulo "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("O triangulo deu certo")
else:
    print(f"Deu não man")
    '''

'''
#49
lado1 = int(input("De o primeiro lado do triangulo "))
lado2 = int(input("De o segundo lado do triangulo "))
lado3 = int(input("De o terceiro lado do triangulo "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("O triangulo deu certo")
    if lado1 == lado2 == lado3:
        print("Tipo: Equilátero")
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("Tipo: Escaleno")
    else:
        print("Tipo: Isósceles")
else:
    print("Não é possivel desvendar oque vc fez ai n ")
'''

'''
#50
salario = int(input("Fale um salario: "))
if salario <= 2000:
    print("isento")
elif salario <= 4000:
    resultado = salario * 0.10
    imp = salario - resultado 
    print(f"O imposto é de R$ {resultado}")
else:
    resultado = salario * 0.20
    imp = salario - resultado
    print(f"O imposto é de R$ {resultado}")
    print(f"o resto do salario é de R$ {imp}")
    '''

'''
#51
for sla in range(10,-1,-1):
    print(sla)
    '''

'''
#52
for sla in range(10,-1,-1):
    print(sla)
print("Fim")
'''

'''
#53
for pares in range(0,101,2):
    print(pares)
'''

'''
#54
for impares in range(1,100,2):
    print(impares)
'''

'''
#55
numero = int(input("Digite um numero para ver a tabuada "))
for i in range(1,11):
    resultado = numero * i
    print(F"{numero} X {i} = {resultado}")
'''

#56

'''
n = int(input("Digite um numero para ver as somas de um ate ele (N) "))
soma = 0

for i in range(1, n + 1):
    soma = soma + i 

print(f"A soma de 1 até {n} é: {soma}")
'''

'''
#57
numero = int(input("Digite um numero não negativo para sabe seu fatorial"))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
    print(f"O fatorial de {numero} é: {fatorial}")
    '''

'''
#58
pares = 0
for i in range(10):
    numero = int(input(f"Digite o {i + 1} Numero: " ))
    if numero % 2 == 0:
        pares += 1

print(f"Você tem {pares} Numeros pares")
       '''

'''
#59
soma_numero = 0
for i in range(10):
    numero = int(input(f"Digite o {i + 1} "))
    if numero > 0:
        soma_numero += numero

print(f"a soma e todos os seus numeros positivos são: {soma_numero}")
'''

'''
#60
maior = None
for i in range(5):
    numero = int(input(f"Digite o {i + 1} numero: "))
    if maior is None or numero > maior:
        maior = numero

        print(f"o maior numero que você digitou foi: {maior}")
'''

'''
#61
menor = None

for i in range(5):
    numero = int(input(f"Digite o {i + 1} numero: "))
    if menor is None or numero < menor:
        menor = numero

        print(f"o menor numero que você digitou foi: {menor}")
'''

'''
#62
soma_notas = 0.0
for i in range(5):
    nota = float(input(f"Digite a sua {i + 1} nota para saber a media e o total "))
    soma_notas += nota
media = soma_notas / 5
print(f"a soma das suas notas é: {soma_notas} e a media delas é: {media} ")
'''

'''
#63                         
senha = ''
while (senha != 1234):
    senha = int(input("Digite a sua senha "))
print("Acesso permitido")
'''

'''
#64
numero = 0
while (numero <= 0):
    numero = int(input(f"É o seguinte, c só passa se seu numero for positivo, saco? "))
print(f"Parabéns, c passou")
'''

'''
#65
opcao = -1

while opcao != 0:
    print("--- MENU ---")
    print("1 - Dizer ola")
    print("2 - Mostrar uma mensagem")
    print("0 - Sair.")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Olá! Seja bem-vindo(a)")
    elif opcao == 2:
        print("estou cansado chefe")
    elif opcao == 0:
        print("Saindo do programa... Até mais!")
    else:
        print("Opção inválida. Tente novamente.")

'''

'''
#66
soma_numero = 0
numero = -1
while numero != 0:
    numero = int(input(f"Coloque quantos numeros quiser (positivos) que irá somar e mostrar o resultado final. "))
    soma_numero += numero
print(f"A soma de todos os numeros que você colocou deu: {soma_numero} ")
'''

'''
#67
soma_notas = 0
notas = -2
quantidade = 0
while notas != -1:
    notas = int(input(f"Digite suas notas e eu vou te falar a soma delas e a media, digite -1 para parar "))
    if notas != -1:
     soma_notas += notas
     quantidade += 1 

media = soma_notas / quantidade
print(f"a soma das suas notas é: {soma_notas} já a media delas é: {media}")
'''

'''
#68
numero_secreto = -1

while numero_secreto != 143:
    numero_secreto = int(input(f"De um palpite de um numero secreto e eu te falo se ele é maior ou menor que o numero em questão "))
    if numero_secreto < 143:
        print("O numero fornecido é menor que o numero secreto ")
    elif numero_secreto > 143:
        print("O numero fornecido é maior que o numero secreto ")
    else:
        print(f"boa man, acertou.")

'''

'''
# 69. Primo
numero = int(input("Digite um numero maior que 1 e eu te falo se ele é primo ou não: "))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print("É primo")
else:
    print("Não é primo")
'''

'''
#70
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for numero in range(inicio, fim + 1):
    if numero > 1:
        divisores = 0
        
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores += 1

        if divisores == 2:
            print(numero)
            '''

'''

#71
nome = "cesar"
print(len(nome))
'''

'''
#72
nome = "felipe"
print(nome.upper())
print(nome.lower())
'''

'''
#73
nome = "cesar"
print(nome[len(nome) - 1])
print(nome[0])
'''

'''
#74
nome = "Raphael"
print(nome.lower().count("a"))
'''

'''
#75
nome = input("Digite uma palavra/nome (qualquer uma):")
if (nome == nome [:: -1]):
    print("A palavra é palíndromo")
else:
    print("A palavra não é palíndromo")
'''
'''
#76
texto = "Eu gosto de jogar"

palavras = texto.split()

quantidade_de_palavras = len(palavras)

ultima_gaveta = quantidade_de_palavras -1

for i in range(ultima_gaveta, -1, -1):
    print(palavras[i])
'''
'''
#77
texto = input("Digite alguma coisa:")
novotexto = texto.split()
print(novotexto)
'''

'''
#78
palavra = input("Digite uma palavra:")
print(len(palavra))
'''

'''
#79
frase = input("Digite uma frase: ")
antiga = input("Frase a ser substituída: ")
nova = input("Nova palavra: ")
print(frase.replace(antiga, nova))
'''

'''
#80
email = input("Digite seu e-mail: ")
if "@" in email and "." in email.split("@")[-1]:
    print("E-mail válido")
else:
    print("E-mail inválido")
'''

'''
#81
lista = ["César", "Jõao", "Felipe", "Micael", "Gabriel"]
for nome in lista:
 print(f"{nome}")
'''

'''
#82
lista = []
for nome in range(5):
 nome = input("Digite 5 nomes ai pra lista pae: ")
 lista.append(nome)
print(lista)
'''

'''
#83
numeros = [10,20,30, 40]
soma = 0
for n in numeros:
 soma += n
print(soma)
'''

'''
#84
numero = [10,30,22,88,100,221,325,908,780,1029,1030]
maior = 0
for nsei in numero:
    if nsei > maior:
        maior = nsei
print(maior)
'''

'''
#85
numero = [10,30,22,88,100,221,325,908,780,1029,1030]
menor = numero[0]
for memacoisa in numero:
    if memacoisa < menor:
        menor = memacoisa
print(menor)
'''

'''
#86
lista = []
soma = 0
for nota in range(5):
    nota = int(input(F"Digite a sua {nota + 1} nota para saber a media: "))
    lista.append(nota)
    soma += nota
media = soma /5
print(f"A media dos seus numeros é: {media}")    
'''

'''
#87
numeros = [1, 4, 7, 10, 15, 18, 22]
pares = []
for abacate in numeros:
    if abacate % 2 == 0:
        pares.append(abacate)
print(f"os numeros que você digitou, esses são pares: {pares}")    
'''

'''
#88
nomes = ["César", "Felipe", "João", "Micael", "Gabriel"]
removedor = input(f"Digite um nome para remove-lo: ")
if removedor in nomes:
    nomes.remove(removedor)
    print(f"{nomes}")
else:
    print(f"Por favor coloque um nome que está na lista!")    
'''

'''
#89
produtos = []

for produto in range (5):
    nome =  input(f"Digite {produto + 1} produtos e eu os colocarei em uma pequena lista!: " )
    produtos.append(nome)
   
print(f"{produtos}")

busca = input(f"Coloque um nome de um produto para saber se ele foi cadastrado: ")
if busca in produtos:
    print(f"o Produto está cadastrado")
else:
    print(f"Produto não está cadastrao! ")
'''

'''
# 90. Ordenação de lista
numeros = []

for i in range(6):
    numero = int(input(f"Digite o {i + 1} numero para ter sua ordem crescente e decrescente: "))
    numeros.append(numero)

numeros.sort()
print(f"Crescente: {numeros}")

numeros.sort(reverse=True)
print(f"Decrescente: {numeros}")
'''

'''
#91
numeros = set()
for i in range (10):
 numero = int(input(f"Digite o {i + 1} número para os numeros distintos: "))
 numeros.add(numero)
print(f"numeros distintos: {numeros}")
'''

'''
#92
conjunto1 = {10,20,30,40,50,60,70,80}
conjunto2 = {20,40,60,80,100,120,140,180}

comuns = conjunto1 & conjunto2

print(f"os numeros que aparecem nos dois conjuntos são os: {comuns}")
'''

'''
#93
tupla = (10,20)

print(f"X: {tupla[0]}")
print(f"y: {tupla[1]}")
'''

'''
#94
dicionario = {
     "nome": "César",
     "idade": 15,
     "cidade": "Uberlândia",
}

print(f"o nome é {dicionario['nome']} a idade é {dicionario['idade']} e mora em {dicionario['cidade']}")
'''

'''
#95
nome = input(f"coloque o nome do aluno: ")
nota1 = int(input(f"coloque a primeira nota do aluno: "))
nota2 = int(input(f"coloque a segunda nota do aluno: "))

aluno = {
    "nome": nome,
    "nota1": nota1,
    "nota2": nota2
}
aluno["media"] = (aluno["nota1"] + aluno["nota2"]) /2

print(f"{aluno['nome']}")
print(f"{aluno['nota1']}")
print(f"{aluno['nota2']}")
print(f"{aluno['media']}")
'''

'''
#96
produtos = [
    {"nome": "teclado", "preco": 150.0},
    {"nome": "mouse", "preco": 35.0},
    {"nome": "monitor", "preco": 250.0},
]

for i in produtos:
    print(f"Produtos: {i['nome']} preços {i['preco']}")
'''

'''
#97
produtos = [
    {"nome": "teclado", "preco": 150.0},
    {"nome": "mouse", "preco": 35.0},
    {"nome": "monitor", "preco": 250.0},
    {"nome": "mouse-pad", "preco": 25.0},
]

mais_caro = produtos[0]

for i in produtos:
    if i["preco"] > mais_caro["preco"]:
        mais_caro = i
print(f"O produto mais caro é: {mais_caro}")
'''

'''
#98
agenda = {
    "cesar": "34 98834-1293",
    "gabriel": "34 9673-1341"
}
buscar = input(f"Digite o nome da pessoa para descobrir o seu número:\n ").lower()
telefone = agenda.get(buscar)

if telefone:
    print(f"o telefone de {buscar.capitalize()} é {telefone}")
else:
    print(f"desculpe, a pessoa {buscar.capitalize()} que você colocou não foi encontrado.")

'''

'''
#99
frase = input(f"Digite uma palavra: ")
palavras = frase.split()

contagem = {}

for i in palavras:
    if i in contagem:
        contagem[i] += 1
    else: contagem[i] = 1
print(f"{contagem}")
'''

'''
#100
estoque = {
    "teclado": 10,
    "mouse": 5,
    "monitor": 2,
}

produto = input(f"Digite o nome do produto que você quer: ")
quantidade = int(input(f"Digite a quantidade de produtos que você quer: "))

if produto in estoque:
    if quantidade <= estoque[produto]:
        estoque[produto] -= quantidade
        print(f"Retirada feita com sucesso! Estoque atual de {produto}: {estoque[produto]}")
    else:
        print(f"Quantidade insuficiente! Temos apenas {estoque[produto]} em estoque.")
else:
    print("Produto não encontrado no estoque.")

'''

'''
#101
def saudacao ():
    print(f"Saudações meu caro, Tudo bem com Você?")
saudacao()
'''

'''
# 102. Saudação com nome
def saudacao(nome):
    print(f"Saudações {nome}, seja bem vindo!")

saudacao("César")
'''

'''
#103
def numeros(a,b):
    return a + b

resultado = numeros(5,3)

print(f"{resultado}")
'''

'''
#104
def maior(a,b):
    if a > b:
        return a
    else:
        return b
resultado = maior(10,25)
print(f"O maior número é: {resultado}")
'''

'''
#105
def numero(a):

    if a %2 == 0:
        return "par"
    else:
        return "ímpar"

resultado = numero(1)
print(f"O numero é {resultado}")
'''

'''
#106
def numero(a,b,c):
    return (a + b + c) / 3
num1 = float(input(f"Digite um numero ai "))
num2 = float(input(f"Digite um numero ai "))
num3 = float(input(f"Digite um numero ai "))
print(f"{numero(num1, num2, num3):.2f}")
'''

'''
#107
def vitor(a,b):
    return a * b
altura = float(input("Digite a altura do seu retangulo "))
base = float(input("Digite a Base do seu retangulo "))
resultado = base * altura
print(f"deu: {resultado} ")
'''

'''
#108
def nsei(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
resultado = nsei(30)

print(f"30°C correspondem a {resultado}°F")
'''

'''
# 109. Fatorial em função
def calcularofatoriazin(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial  # Fora do loop para retornar o valor final completo

resultado = calcularofatoriazin(5)
print(f"o fatorial é: {resultado}")
'''

'''
# 110. Verificar primo
def primo(A):
    if A <= 1:
        return False

    for i in range(2, A):
        if A % i == 0:
            return False

    return True

resultado = primo(7)
print(f"O número é primo? {resultado}")
'''

'''

# 111. Contar vogais
def vogal(n):
    vogais = "aeiouAEIOU"
    total = 0

    for letra in n:
        if letra in vogais:
            total += 1
            
    return vogal_total  
     return total

resultado = vogal("Python")
print(f"Quantidade de vogais: {resultado}")
'''

'''
# 112. Maior valor de lista
def maior_valor(lista):
    if not lista:
        return None
    maior = lista[0]

    for num in lista:
        if num > maior:
            maior = num
    return maior

numeros = [40, 50, 11, 67, 30, 19, 20]
resultado = maior_valor(numeros)
print(f"O maior valor é: {resultado}")
''' 

'''
#113
def calcular_media(lista):
    if not lista: 
        return 0
    
    soma = sum(lista)
    quantidade = len(lista)
    
    return soma / quantidade

notas = [10, 8, 6, 4]
resultado = calcular_media(notas)
print(f"A média é: {resultado}")

vazia = []
resultado_vazia = calcular_media(vazia)
print(f"Média de lista vazia: {resultado_vazia}")    
'''

'''
#114
def filtrar_positivos(lista):
    positivos = []
    
    for num in lista:
        if num > 0:
            positivos.append(num)  
            
    return positivos

numeros = [-10, 15, -3, 0, 8, -1, 42]
resultado = filtrar_positivos(numeros)

print(f"Lista de positivos: {resultado}")
'''

'''
#115
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b


print("--- CALCULADORA ---")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Escolha uma opção (1-4): ")


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))


if opcao == "1":
    resultado = somar(n1, n2)
    print(f"Resultado: {n1} + {n2} = {resultado}")
elif opcao == "2":
    resultado = subtrair(n1, n2)
    print(f"Resultado: {n1} - {n2} = {resultado}")
elif opcao == "3":
    resultado = multiplicar(n1, n2)
    print(f"Resultado: {n1} * {n2} = {resultado}")
elif opcao == "4":
    resultado = dividir(n1, n2)
    print(f"Resultado: {resultado}")
else:
    print("Opção inválida!")
'''

'''
#116
nome = input(f"Digite seu nome para criar um arquivo txt ai: ")
with open("nomes.txt", "w") as arquivo:
    arquivo.write(nome)

print(f"Nome foi cadastrado com sucesso!")
'''

'''
#117
with open("nomes.txt", "a") as arquivo:
    while(True):
        nome = input("Digita um nome denovo ai man, se digitar 'sair' vai parar. ")

        if nome.lower() == 'sair':
            break

        arquivo.write(nome + "\n")
'''

'''
#118
with open("nomes.txt", "r") as arquivo:
    laele = arquivo.read()
print(f"{laele}")

'''

'''
#119
with open("nomes.txt", "r") as arquivo:
  for nseind in arquivo:
    print(nseind.strip())
'''

'''
#120
with open("nomes.txt", "r") as arquivo:
    verlinhas = arquivo.readlines()

print(len(verlinhas))
'''

'''
#121
try:
    numero = int(input(f"Digite um numero INTEIRO "))
    print(f"Eu realmente amava ela")
except ValueError:
    print(f"Eu falei inteiro poh")
'''

'''
#122
try:
    numero1 = int(input(f"Digite um numero que seja dividido pelo o outro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    resultado = numero1 / numero2
    print(resultado)

except ValueError:
    print(f"Digite um Valor valido.")

except ZeroDivisionError:
    print(f"oh lenda, me explica como que vai dividir por 0")

'''

'''
#123
import calculos

resultado = calculos.nsei(10,5)
resultado2= calculos.multiplicar(10, 12)
print(f"{resultado}")
print(f"{resultado2}")
'''

'''
# 124. Primeira classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("César", 15)
print(f"O nome é {pessoa1.nome}")
print(f"A idade é {pessoa1.idade}")

'''

'''
#125
class pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 =  pessoa("César", 15)
pessoa2 = pessoa("Gabriel", 17)
print(f"O nome é {pessoa1.nome}")
print(f"A idade é {pessoa1.idade}")

print(f"O nome é {pessoa2.nome}")
print(f"A idade é {pessoa2.idade}")


'''

'''
#126
class pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):      
     print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

pessoa1 =  pessoa("César", 15)
pessoa1.apresentar()
'''

'''
#127
class produtos:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def mostrar(self):
     print(f"nome do produto: {self.nome} e o preço é {self.preco}")
   


produto1 = produtos("Picanha", 100)
produto2 = produtos("weyprotein", 60)
produto3 = produtos("O Amor dela (não é comprável)", 100)

produto1.mostrar()
produto2.mostrar()
produto3.mostrar()
'''

'''
#128
class produtos:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def mostrar(self):
     print(f"nome do produto: {self.nome} e o preço é {self.preco}")

    def valor_desconto(self, percentual):
       desconto = self.preco * (percentual / 100)
       self.preco -= desconto

print(f"Antes do desconto:")
produto3 = produtos("O Amor dela (não é comprável)",100)
produto3.mostrar()

produto3.valor_desconto(10)
print(f"Depois do desconto")
produto3.mostrar()

'''

'''
# 129. Conta bancária
class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar_valor(self, valor):
        self.saldo += valor

    def sacar_valor(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Dinheiro retirado com sucesso!")
        else:
            print("Deu ruim, saldo insuficiente.")

'''
# 130. Aluno
'''
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def calcular_media(self):
        soma = sum(self.nota)
        quantidade = len(self.nota)
        return soma / quantidade

aluno1 = Aluno("César", [8, 8, 8])
media_total = aluno1.calcular_media()  # Chamando o método no objeto correto com ()

print(f"O aluno {aluno1.nome} ficou com a média: {media_total}")
'''

'''
#131
class aluno:
    def __init__(self,nome,nota):
        self.nome = nome
        self.nota = nota
    def calcular_media(self):
        soma = sum(self.nota)
        quantidade = len(self.nota)
        return soma / quantidade
    def apro_repro(self):
        media = self.calcular_media()
        if media >= 6:
            return "aprovado"
        else:
            return "reprovado" 
aluno1 = aluno("César", [8, 8, 8])
print(f"Média: {aluno1.calcular_media()}")
print(f"Situação do aluno: {aluno1.apro_repro()}")
'''
# 132. Retângulo
'''
class Retangulo:

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura

    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)  # Corrigido para somar todos os lados


retangulo1 = Retangulo(15, 15)
print(f"A área é: {retangulo1.calcular_area()}")
print(f"O perímetro é: {retangulo1.calcular_perimetro()}")

'''
# 133. Carro
'''
class Carro:

    def __init__(self, modelo, velocidade_atual, velocidade_maxima):
        self.modelo = modelo
        self.atual = velocidade_atual
        self.maxima = velocidade_maxima

    def acelerar(self, valor):
        if self.atual + valor > self.maxima:
            self.atual = self.maxima
        else:
            self.atual += valor

    def frear(self, valor):
        self.atual -= valor
        if self.atual < 0:  # Indentação corrigida para dentro da função
            self.atual = 0


# 134. Biblioteca
class Livro:

    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel


class Biblioteca:

    def __init__(self):
        self.livros = []  # Nome corrigido para plural

    def adicionar(self, livro):
        livro.disponivel = True
        self.livros.append(
            livro
        )  # Corrigido de self.livro para self.livros
        print("Livro foi adicionado com sucesso")

    def listar(self):
        for livro in self.livros:
            print(f"- {livro.titulo} (Disponível: {livro.disponivel})")

    def emprestar(self, emprestimo):
        if emprestimo in self.livros:
            posicao = self.livros.index(emprestimo)
            self.livros[posicao].disponivel = (
                False  # Corrigido de disponive para disponivel
            )
            print(f"'{emprestimo.titulo}' emprestado com sucesso!")
        else:
            print("Deu ruim, parça. Livro não encontrado.")

    def devolver(self, devolvido):
        if devolvido in self.livros:
            posicao = self.livros.index(devolvido)
            self.livros[posicao].disponivel = (
                True  # Corrigido de disponive para disponivel
            )
            print("Livro devolvido com sucesso!")
        else:
            print("Esse livro não está cadastrado.")

'''
# 135. Sistema de Produtos (Menu Completo)
'''
class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produtos = []

while True:
    print("\n--- SISTEMA DE PRODUTOS ---")
    print("1. Cadastrar novo produto")
    print("2. Listar todos os produtos")
    print("3. Buscar produto por nome")
    print("4. Calcular valor total do estoque")
    print("5. Sair")

    opcao = input("Escolhe uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: R$ "))
        p = Produto(nome, preco)
        produtos.append(p)
        print(f"Produto '{nome}' cadastrado com sucesso!")

    elif opcao == "2":
        if not produtos:
            print("Ainda não há produtos cadastrados.")
        else:
            print("\n--- LISTA DE PRODUTOS ---")
            for p in produtos:
                print(f"- {p.nome} | R$ {p.preco:.2f}")

    elif opcao == "3":
        busca = input("Qual o nome do produto que procuras? ").lower()
        encontrado = False
        for p in produtos:
            if p.nome.lower() == busca:
                print(
                    f"Encontrado! O produto {p.nome} custa R$ {p.preco:.2f}."
                )
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "4":
        total = 0
        for p in produtos:
            total += p.preco
        print(f"\nO valor total de todos os produtos é: R$ {total:.2f}")

    elif opcao == "5":
        print("A encerrar o sistema. Até logo!")
        break
    else:
        print("Opção inválida, tenta de novo.")
'''