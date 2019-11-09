#Faça um prog que leia vários n° inteiros.
#O prog só vai parar quando o usuário digitar o valor 999,que é a condição de parada.
#No final, mostre quantos n° foram digitados e qual foi a soma entre eles(desconsiderando o 999).
num = cont = soma = 0

while num != 999:
    num = int(input('digite o n°(Para sair, digite 999):'))
    if num != 999:
        cont += 1
        soma += num
print('Quantidade de n° digitados: {}\nSoma total dos valores: {}'.format(cont,soma))