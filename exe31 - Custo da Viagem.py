'''Crie um prog leia a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas.'''

km=float(input('Digite a distância Km:'))
if km<=200:
    pa=km*0.5
    print('Valor da passagem 0.5: R${:.2f}'.format(pa))
else:
    pa=km*0.45
    print('Valor da passagem 0.45: R${:.2f}'.format(pa))