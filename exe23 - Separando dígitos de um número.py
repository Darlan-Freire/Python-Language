#Faça um prog que leia um numero de 0 a 9999 e mostre cada um dos elementos separados.
#EX: digite o n°: 1843
#milhar:1
#centenas:8
#dezenas:4
#unidades:3

num=int(input('Digite o numero de 0 a 9999:'))

print('\nMilhar:',num//1000%10)
print('Centena:',num//100%10)
print('Dezena:',num//10%10)
print('Unidade:',num//1%10)