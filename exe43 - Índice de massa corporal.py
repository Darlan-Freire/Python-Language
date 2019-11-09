#crie um prog que leia o peso e a altura de uma pessoa
#Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
##Entre 18.5 e 25: Peso ideal
#De 25 até 30: Sobrepeso
#De 30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

peso=float(input('Peso:'))
altura=float(input('Altura:'))
imc=peso/altura**2
if imc<=18.50:
    print('IMC: {:.2f} = Abaixo do peso'.format(imc))
elif imc>18.50 and imc<=25:
    print('IMC: {:.2f} = Peso ideal'.format(imc))
elif imc>25 and imc<=30:
    print('IMC: {:.2f} = Sobrepeso'.format(imc))
elif imc>30 and imc<=40:
    print('IMC: {:.2f} = Obesidade'.format(imc))
else:
    print('IMC: {:.2f} = Obesidade Mórbida'.format(imc))