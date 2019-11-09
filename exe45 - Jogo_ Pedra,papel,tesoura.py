#faça um prog que faça o PC jogar Jokenpô com você.
#Pedra, papel ou tesoura.

print('{:=^40}'.format(' J   O   K   E   N   P   Ô '))
import random,time
jokenpo=['Pedra','Papel','Tesoura']
pc=random.choice(jokenpo)
nome=str(input('Digite seu nome:')).strip().title()
op=str(input('___ESCOLHA___\n[1]Pedra\n[2]Papel\n[3]Tesoura\n\nFaça sua escolha:')).strip().title()
print('JOKENPO...1...2...')
time.sleep(2)

print('\nPC: {}   <VS>   {}  :{}'.format(pc,op,nome))
if 'Pedra'==pc and 'Pedra'==op:
    print('\tEMPATE')
elif 'Pedra'==pc and 'Papel'==op:
    print('\t{} WIN'.format(nome))
elif 'Pedra'==pc and 'Tesoura'==op:
    print('\tPC WIN')
elif 'Papel'==pc and 'Pedra'==op:
    print('\tPC WIN')
elif 'Papel'==pc and 'Papel'==op:
    print('\tEMPATE')
elif 'Papel'==pc and 'Tesoura'==op:
    print('\t{} WIN'.format(nome))
elif 'Tesoura'==pc and 'Pedra'==op:
    print('\t{} WIN'.format(nome))
elif 'Tesoura' and 'Papel'==op:
    print('\tPC WIN')
elif 'Tesoura'==pc and 'Tesoura'==op:
    print('\tEMPATE')
else:
    print('Opção inválida. Escolha entre Pedra,Papel ou Tesoura')
