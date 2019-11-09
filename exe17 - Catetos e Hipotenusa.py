#Faça um prog que o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

import math
cat=float(input('Digite o cateto oposto:'))
adj=float(input('Digite o cateto adjacente:'))
#hip=math.hypot(cat,adj)
print('Comprimento da hipotenusa: {:.2f}'.format(math.hypot(cat,adj)))



