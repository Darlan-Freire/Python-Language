#Faça um prog que leia um n° inteiro e diga se ele é ou não um n° primo.
cont=0
num=int(input('Digite um n° inteiro:'))
for c in range(1,num+1):
    if num % c == 0:
        cont+=1
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end=' ')
if cont == 2:
    print('\n\033[m{} É PRIMO'.format(num))
else:
    print('\n\033[m{} NÃO É PRIMO'.format(num))
