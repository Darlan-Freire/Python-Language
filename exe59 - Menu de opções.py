#Crie o prog que leia 2 valores e mostre um menu na tela:
#[1]somar
#[2]multiplicar
#[3]dividir
#[4]maior
#[5]sair do programa
#Seu prog deverá realizar a operação solicitada em cada caso.

n1 = int(input('digite o 1° valor:'))
n2 = int(input('digite o 2° valor:'))
op = 0
while op != 5:
    op = int(input('''
[1]somar
[2]multiplicar
[3]dividir
[4]maior
[5]sair do programa

Digite a opção:'''))
    if op == 1:
        print('A soma de {} + {} = {}'.format(n1,n2,n1+n2))
    elif op == 2:
        print('A multiplicação de {} X {} = {}'.format(n1,n2,n1*n2))
    elif op == 3:
        print('A divisão entre {} / {} = {}'.format(n1,n2,n1/n2))
    elif op == 4:
        if n1>n2:
            print('{} é MAIOR'.format(n1))
        else:
            print('{} é MAIOR'.format(n2))
print('fim')