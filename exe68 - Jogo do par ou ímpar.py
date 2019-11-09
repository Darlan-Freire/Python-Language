#Faça um prog que jogue PAR OU ÍMPAR.
#O jogo só será interrompido quando o jogador PERDER.
#Mostrando o total de vitórias consecutivas que ele conseguiu no final.

from random import randint
vitoria = 0

print('*'*25)
print('<<<JOGO DO PAR OU ÍMPAR>>>')
print('*'*25)

while True:
    jogador_num = int(input('\nDigite o n° entre 1 e 10:'))
    cpu = randint(1,10)
    total = cpu + jogador_num
    jogador_op = ' '
    #print(f'Você: {jogador_num} - CPU: {cpu} - Total: {total}')
    while jogador_op not in 'PI':
        jogador_op = str(input('PAR[P] OU ÍMPAR[I]:')).strip().upper()[0]
    if jogador_op == 'P':
        if total % 2 == 0:
            vitoria += 1
            print(f'\nVENCEU :D !!!\nJogador: {jogador_num}\nCPU: {cpu}\nResultado: {total}')
        else:
            break
    elif jogador_op == 'I':
        if total % 2 == 1:
            vitoria += 1
            print(f'\nVENCEU :D !!!\nJogador: {jogador_num}\nCPU: {cpu}\nResultado: {total}')
        else:
            break
    print('Vamos jogar novamente!')
print(f'\nPERDEU :( !!!\nJogador: {jogador_num}\nCPU: {cpu}\nResultado: {total}\nTotal de vitórias: {vitoria}')