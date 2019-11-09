#Crie um prog que leia algo pelo teclado e mostre na tela seu tipo primitivo e
#todas as informações possíveis sobre ela.

algo=input('Digite algo: \n')
print(type(algo))
print(algo.isalpha())
print(algo.isnumeric())
print(algo.isdecimal())
print(algo.islower())
print(algo.istitle())
print(algo.isupper())
