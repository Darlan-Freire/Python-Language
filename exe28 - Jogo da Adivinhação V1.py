#Crie um prog que pense em um n° inteiro, entre 0 e 5 e peça para o usuário descobrir qual n° foi escolhido.
#O prog deve escrever se o usuário venceu ou perdeu.

from time import sleep
from random import randint

print('*****Sorteando Número*****')
n=randint(1,5)
num=int(input('\nAdivinhe o número:'))
print('3, 2, 1....')
sleep(2)
if num==n:
    print('PARABÉNS! O n° sorteado é:',n)
else:
    print('ERRADO... Tente novamente!')