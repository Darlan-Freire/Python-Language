#Crie um prog que leia quanto dinheiro uma pessoa tem na carteira e
#mostre quantos dólares ela pode comprar
#Considere: US$ 1,00 == R$ 3,27

valor=float(input('Digite o valor R$'))
dolar= valor/3.27
print('Dólares que pode comprar: US$ {:.2f}'.format(dolar))


