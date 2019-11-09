#Faça um prog que leia 3 n° e diga qual é o menor e qual é o maior.

n1=int(input('Digite n1:'))
n2=int(input('Digite n2:'))
n3=int(input('Digite n3:'))
#Testa quem é maior
if n1>n2 and n1>n3:
    M=n1
elif n2>n1 and n2>n3:
    M=n2
elif n3>n1 and n3>n2:
    M=n3
else:
    print('Existe números iguais')
#Testa quem é menor
if n1<n2 and n1<n3:
    m=n1
elif n2<n1 and n2<n3:
    m=n2
elif n3<n1 and n3<n2:
    m=n3
else:
    print('Existe n°s iguais')
print('\nMAIOR: {}\nmenor: {}'.format(M,m))