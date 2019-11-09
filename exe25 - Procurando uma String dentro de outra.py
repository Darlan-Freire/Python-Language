#Crie um prog que leia o nome completo de uma pessoa e diga se existe 'SILVA' no nome

nome=str(input('Digite nome completo:')).strip()
print('Existe \'SILVA\':','SILVA' in nome.upper())