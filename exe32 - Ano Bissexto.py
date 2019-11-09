#Faça um prog que leia um ano qualquer e diga se ele é um ano BISSEXTO.
from datetime import date
ano=int(input('Digite o ano:'))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('{} É BISEXTO'.format(ano))
else:
    print('{} NÃO É BISSEXTO'.format(ano))
