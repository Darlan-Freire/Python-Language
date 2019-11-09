#Faça um prog que leia um número N inteiro qualquer
#E mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#Ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
i = fibonacci = f1 = total = 0
f2=1
termo=-1

while termo != 0:
    total+=termo
    while i <= total:
        fibonacci = f1 + f2
        print('{}'.format(fibonacci),end=' > ')
        f2 = f1
        f1 = fibonacci
        i+=1
    termo = int(input('\ndigite n° de termos, ou [0] para SAIR:'))
print('fim')
