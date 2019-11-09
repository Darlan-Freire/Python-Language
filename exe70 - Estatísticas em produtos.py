#Crie um prog que leia o NOME e o PREÇO de VÁRIOS PRODUTOS.
#O prog deverá perguntar se o USUÁRIO vai continuar.
#No final, mostre:
# (a) Qual é o TOTAL DE GASTO na compra.
# (b) Quantos produtos custam MAIS de R$1000.
# (c) Qual é o NOME do produto mais BARATO.
total = MaiorMil = menor = cont = 0
produto = ' '
while True:
    nome = str(input('nome do produto:')).strip().title()
    custo = float(input('preço R$:'))
    total += custo
    cont += 1
    if custo > 1000:
        MaiorMil += 1
    if cont == 1 or custo < menor:
        menor = custo
        produto = nome
    print('Cadastro com SUCESSO')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\n(a)Total gasto: {total}\n(b)Produtos custando mais de mil: {MaiorMil}\n(c)Nome do produto mais barato: {produto}')
