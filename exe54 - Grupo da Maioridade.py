#Faça um prog que leia o ano de nasc de 7 pessoas.
#No final,mostre quantas pessoas ainda não atingiram a maioridade
# E quantas já são maiores, considerando a idade de 21 anos.
import datetime
x=datetime.date.today().year
menor=0
maior=0
for c in range(0,7):
    nasc=int(input('Digite o ano de nascimento:'))
    if x-nasc < 21:
        menor+=1
    else:
        maior+=1
print('{} pessoas, ainda NÃO atingiram a maioridade\n{} pessoas, SÃO maiores de idade'.format(menor,maior))


