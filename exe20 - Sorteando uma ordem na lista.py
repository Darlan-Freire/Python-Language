#O mesmo professor do exe anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um prog que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1=str(input('Nome aluno:'))
n2=str(input('Nome aluno:'))
n3=str(input('Nome aluno:'))
n4=str(input('Nome aluno:'))

lista=[n1,n2,n3,n4]
shuffle(lista)
print('Ordem de apresentação: {}'.format(lista))

