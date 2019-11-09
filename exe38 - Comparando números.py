#Crie um prog que leia dois n° inteiros e compare-os, mostrando uma mensagem:
#O primeiro valor é maior, o segundo é menor, não existe pois os dois valores são iguais

x=int(input('Digite o n°:'))
y=int(input('Digite o n°:'))

if x<y:
    M=y
    m=x
    print('M = {}\nm = {}'.format(M,m))
elif y<x:
    M=x
    m=y
    print('M = {}\nm = {}'.format(M,m))
else:
    print('VALORES IGUAIS')

