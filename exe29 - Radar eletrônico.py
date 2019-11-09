#Crie um prog que leia a velocidade de um carro
#Se ele ultrapassar 80Km/h,imprima que ele foi multado
#A multa vai custar R$7,00 por cada Km acima do limite.

vel=int(input('Digite a velocidade Km/h:'))
if vel>80:
    print('VC FOI MULTADO!')
    multa=(vel-80)*7
    print('Valor à pagar: R$',multa)
else:
    print('VC ESTÁ DENTRO DOS LIMITES DE VELOCIDADE')
