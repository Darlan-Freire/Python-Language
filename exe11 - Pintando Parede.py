#Faça um prog que leia a largura e altura de uma parede em metros.
#Calcule sua área e a quantidade de tinta necessária para pinta-lá.
#Sabendo que cada litro de tinta, pinta uma área de 2m²

larg=float(input('Digite a Largura da parede:'))
alt=float(input('Digite a Altura da parede:'))
area=larg*alt
print('A área da sua parede é de: {}m²\nQuantidade necessária para pintar a parede é de: {}l'.format(area,area/2))

