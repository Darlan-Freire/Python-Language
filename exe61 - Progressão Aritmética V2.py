#Refaça o exe51, lendo o primeiro termo e a razão de uma PA
#Mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('digite o termo:'))
razao = int(input('digite a razão:'))
i=0

while i < 10:
    print(termo,end=' > ')
    termo += razao
    i+= 1
print('Acabou')
