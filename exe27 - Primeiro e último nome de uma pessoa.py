#Faça um prog que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente

nome=str(input('Digite seu nome completo:')).strip()
nome=nome.split()
print('Primeiro nome:',nome[0])
print('Último nome:',nome[len(nome)-1])
