#Faça um prog que leie um ângulo qualquer e mostre o valor de seno, cosseno e tangente desse ângulo.

import math
a=float(input('Digite o ângulo:'))
sen=math.sin(math.radians(a))
con=math.cos(math.radians(a))
tan=math.tan(math.radians(a))
print('\nSeno:{:.2f}\nCosseno:{:.2f}\nTangente:{:.2f}'.format(sen,con,tan))
