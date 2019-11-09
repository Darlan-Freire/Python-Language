#Faça um prog que leia uma frase e mostre:
#Quantas vezes aparece a letra 'a'
#Em que posição o 'a' aparece na primeira vez
#Em que posição aparece a última vez

frase=str(input('Digite a frase:')).lower().strip()
print('A letra \'a\' aparece: {} vezes'.format(frase.count('a')))
print('Primeira \'a\' está no [i]: {}'.format(frase.find('a')+1))
print('Último \'a\' está no [i]: {}'.format(frase.rfind('a')+1))