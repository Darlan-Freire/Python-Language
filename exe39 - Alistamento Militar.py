#Faça um prog que leia o ano de nascimento de um jovem e informe, de acordo com usa idade:
#Se ele ainda vai se alistar.
#Se é a hora de se alistar.
#Se já passou do tempo de se alistar.
#O prog deverá tbm informar o tempo que falta ou que passou do prazo.

import datetime

nasc=int(input('Digite o ano de nascimento:'))
anoatual=datetime.date.today().year
id=anoatual-nasc
if id<18:
    print('Você ainda irá se alistar')
    print('Falta {} anos'.format(18-id))
elif id==18:
    print('É HORA DE SE ALISTAR')
else:
    print('JÁ PASSOU DO TEMPO DE SE ALISTAR')
    print('Está atrasado {} anos'.format(id-18))