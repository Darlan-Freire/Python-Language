#Faça um prog que leia 6 n° iteiros e mostre a soma
#apenas daqueles que forem pares.
#Se o valor digitado for ímoar, desconsidere-o.
par=0
impa=0
contp=0
conti=0
for i in range(1,7):
    n=int(input('Digite o valor:'))
    if n%2==0:
        contp+=1
        par+=n
    else:
        conti+=1
        impa+=n
print('\nQtd n° Pares {} - Total: {}\nQtd n° Impar {} - Total: {}'.format(contp,par,conti,impa))


