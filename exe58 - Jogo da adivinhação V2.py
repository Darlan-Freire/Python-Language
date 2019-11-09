#Refaça o exe28, onde o CPU vai "sortear" em um n° entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar.
#Mostrando no final quantos palpites foram necessários para vencer.

from time import sleep
from random import randint

print('===SORTEANDO O NÚMERO ENTRE 1...1000===')
n = randint(1,1000)
num = 0
cont = 0
while num != n:
    num = int(input("Digite o número:"))
    if num == n:
        print('PARABÉNS! Número sorteado é: {}\nN° de tentativas erradas: {}'.format(n,cont))
    else:
        print('ERRADO, TENTE NOVAMENTE')
        cont += 1
        if num < n:
            print('É Mais que {}...\n'.format(num))
        else:
            print('É Menos que {}...\n'.format(num))
print('Fim')