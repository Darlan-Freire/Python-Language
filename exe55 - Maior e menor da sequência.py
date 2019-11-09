#Faça um prog que leia o peso de 5 pessoas.
#No final, mostre qual foi o MAIOR e o MENOR peso lidos.
maior=0
menor=500
for c in range(0,5):
    peso=float(input('Digite o peso:'))

    if peso > maior:
        maior=peso
    elif peso < menor:
        menor=peso
print('Maior peso: {}\nmenor peso: {}'.format(maior,menor))
