#Crie um prog que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com sua idade.
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 25: Sênior
#Acima: Master
import datetime
date=datetime.date.today().year
ano=int(input('Digite seu ano de nascimento:'))
id=date-ano
if id <= 9:
    print('Idade: {} - Mirim'.format(id))
elif id <= 14:
    print('Idade: {} - Infantil'.format(id))
elif id <= 19:
    print('Idade: {} - Junior'.format(id))
elif id <=25:
    print('Idade: {} - Sênior'.format(id))
else:
    print('Idade: {} - Master'.format(id))

