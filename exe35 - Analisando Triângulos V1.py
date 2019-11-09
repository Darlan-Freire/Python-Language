#Crie um prog que leia o comprimento de 3 retas e diga ao usuário se é possível ou não formar um triângulo.

a=float(input('Comprimento reta 1:'))
b=float(input('Comprimento reta 2:'))
c=float(input('Comprimento reta 3:'))

if a<b+c and b<a+c and c<a+b:
    print('TRIÂNGULO')
else:
    print('Não forma triângulo')
