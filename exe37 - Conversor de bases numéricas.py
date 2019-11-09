#crie um prog que leia um n° inteiro qualquer e peça para o usuário escolher a base de conversão:
#1 - para binário
#2 - para octal
#3 - para hexadecimal

num=int(input('Digite o numero em decimal:'))
print('[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\n')
base=int(input('Qual Base?:'))

if base == 1:
    print('Binário: {}'.format(bin(num)[2:]))
elif base == 2:
    print('Octal: {}'.format(oct(num)[2:]))
elif base == 3:
    print('Hexadecimal: {}'.format(hex(num)[2:]))
else:
    print('Opcão inválida!')