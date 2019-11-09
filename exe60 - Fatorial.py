#Faça um prog que leia um n° qualquer e mostre o seu fatorial.
#EX: 5! = 5x4x3x2x1 = 120



'''+++++++Usando uma fução recurssiva+++++++++'''

def fatorial(x):
    if x==0:
        return 1
    else:
        return x*fatorial(x-1)

num=int(input('Digite o numero:'))
print("Fatorial de {} é: {}".format(num,fatorial(num)))


'''OU, usando o while'''

num = int(input('digite o numero:'))
cont = num
f = 1
while cont > 0:
    f *= cont
    cont -= 1
print('Fatorial de {} é = {}'.format(num,f))