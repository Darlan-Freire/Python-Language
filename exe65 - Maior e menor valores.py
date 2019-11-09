#Faça um prog que leia vários n° inteiros.
#No final, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O prog deve perguntar ao usuário se ele quer ou não continuar a digitar os valores.

num = op = soma = cont = M = m = 0
while op != 'N':
    num = int(input('digite o número:'))
    if op != 'N':
        soma += num
        cont += 1
    if cont == 1:
        M = m = num
    elif num < m:
        m = num
    else:
        M = num
    op = str(input('continua a digitar valores? [S/N]:')).upper().strip()
print('\nQuantidade de n° digitados: {}\nSoma total dos valores: {}\nMédia: {:.2}\nMAIOR: {}\nmenor: {}'.format(cont,soma,soma/cont,M,m))