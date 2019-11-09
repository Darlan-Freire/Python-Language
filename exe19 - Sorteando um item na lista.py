#Um professor que sortear um de seus 4 alunos para apagar o quadro.
#Faça um prog que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno1=input('Digite o nome do aluno 1:')
aluno2=input('Digite o nome do aluno 2:')
aluno3=input('Digite o nome do aluno 3:')
aluno4=input('Digite o nome do aluno 4:')

lista=[aluno1,aluno2,aluno3,aluno4]

print('Aluno sorteado: {}'.format(random.choice(lista)))