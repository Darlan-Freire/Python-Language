#Crie um prog que pergunte a quantidade de Km percorrido por um carro alugado.
#e a quantidade de dias que foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km=float(input('Quantidade de Km percorrido:'))
dias=int(input('Quantos dias foi alugado'))
preço=(60*dias)+(0.15*km)
print('Total a pagar R${}'.format(preço))