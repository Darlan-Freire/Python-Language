#Crie um prog que leia o nome completo de uma pessoa e mostre:
#1°O nome com todas as letras em  Maiúsculo
#2°O nome com todas as letras em minúsculo
#3°Quantas letras existem ao todo (Sem considerar espaços)
#4°Quantas letras tem o primeiro nome

nome=input('Digite seu nome completo:').strip()

print('1° letras em M: ',nome.upper())
print('2° letras em m: ',nome.lower())
print('3° Quantidade de letras:',len(nome)-nome.count(' '))
print('4° Primeiro nome tem: {} letras'.format(nome.find(' ')))
#nome=nome.split()
#print('4° Seu primeiro nome tem: {} letras'.format(len(nome[0])))