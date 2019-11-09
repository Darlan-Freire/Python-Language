#Crie um prog que leie um n° real qualquer e mostre a sua porção inteira
#EX: digite um n°: 6.127 - parte inteira = 6

from math import trunc

a=float(input("Digite o n° real: "))
print('Porção inteira: {}'.format(trunc(a)))

