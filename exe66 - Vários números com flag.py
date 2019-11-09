#Faça um prog que leia VÁRIOS N° inteiros. O prog só vai parar quando o usuário digitar 999.
#No final, mostre QUANTOS N° foram digitados e qual foi a SOMA entre eles.
num = soma = cont = 0
while True:
    num = int(input('digite num, ou 999 para sair:'))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'Qtn N°: {cont}\nSoma total: {soma}')
