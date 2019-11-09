#Faça um prog que leia uma frase qualquer e diga se ela é um palíndromo.
#desconsiderando os espaços.
#EX.: APOS A SOPA, A SACADA DA CASA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase=str(input('Digite a frase:')).strip().split()
junto=''.join(frase).upper()
inverso=''

for i in range(len(junto)-1,-1,-1): # len(junto) - Está me dizendo o tamanho string, ou seja,
    inverso+=junto[i]               #se a frase tem 10 letras, a última está no índice 9 pois o 10 é a condição de parada.

if junto==inverso:
    print('PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')